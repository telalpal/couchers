import { render, screen, within } from "@testing-library/react";
import { service } from "service/index";
import wrapper from "test/hookWrapper";
import { getUser, listFriends } from "test/serviceMockDefaults";
import { MockedService } from "test/utils";

import FriendList from "./FriendList";
import { FRIEND_ITEM_TEST_ID } from "./FriendSummaryView";

const createGroupChatMock = service.conversations
  .createGroupChat as MockedService<
  typeof service.conversations.createGroupChat
>;
const listFriendsMock = service.api.listFriends as MockedService<
  typeof service.api.listFriends
>;
const getDirectMessageMock = service.conversations
  .getDirectMessage as MockedService<
  typeof service.conversations.getDirectMessage
>;
const getUserMock = service.user.getUser as MockedService<
  typeof service.user.getUser
>;

describe("FriendList", () => {
  beforeEach(() => {
    listFriendsMock.mockImplementation(listFriends);
    getUserMock.mockImplementation(getUser);
    getDirectMessageMock.mockImplementation(async (userId) => {
      if (userId === 2) return 1;
      throw new Error("Couldn't find that chat.");
    });
    createGroupChatMock.mockResolvedValue(2);
  });

  it("shows a loading indicator when the friend list is still loading", async () => {
    listFriendsMock.mockImplementation(() => new Promise(() => void 0));
    render(<FriendList />, { wrapper });

    expect(await screen.findByRole("progressbar")).toBeVisible();
  });

  it("renders the friend list when all friends are loaded", async () => {
    jest.spyOn(console, "error").mockReturnValue(undefined);
    render(<FriendList />, { wrapper });

    const [firstFriend, secondFriend] = (
      await screen.findAllByTestId(FRIEND_ITEM_TEST_ID)
    ).map((element) => within(element));

    // First friend
    expect(
      firstFriend.getByRole("link", { name: "Funny Dog @funnydog" })
    ).toBeVisible();
    expect(
      firstFriend.getByRole("button", { name: "Direct message" })
    ).toBeVisible();

    // Second friend
    expect(
      secondFriend.getByRole("link", { name: "Funny Kid @funnykid" })
    ).toBeVisible();
    expect(
      secondFriend.getByRole("button", { name: "Direct message" })
    ).toBeVisible();
  });

  // Cases to check:
  // - Negative path UI
  // - spinner on friend item UI if getDirectMessage is still loading
  // - Clicking on link works
  // - Clicking on button creates a new chat if one doesn't exist (no link scenario)
  //   - error snack bar if create fails
});

import { IconButton, Snackbar } from "@material-ui/core";
import Alert from "components/Alert";
import CircularProgress from "components/CircularProgress";
import { EmailIcon } from "components/Icons";
import useCreateGroupChat from "features/messages/groupchats/useCreateGroupChat";
import { Error as GrpcError } from "grpc-web";
import { User } from "pb/api_pb";
import { GroupChat } from "pb/conversations_pb";
import React from "react";
import { useQuery, useQueryClient } from "react-query";
import { Link, useHistory } from "react-router-dom";
import { routeToGroupChat } from "routes";
import { service } from "service/index";
import { useIsMounted, useSafeState } from "utils/hooks";

import { directMessageQueryStaleTime } from "../constants";
import FriendSummaryView from "./FriendSummaryView";
import FriendTile from "./FriendTile";
import useFriendList from "./useFriendList";

function CurrentFriendAction({ friend }: { friend: User.AsObject }) {
  const history = useHistory();
  const queryClient = useQueryClient();
  const { data: groupChat, isLoading } = useQuery<
    GroupChat.AsObject,
    GrpcError
  >({
    cacheTime: directMessageQueryStaleTime,
    staleTime: directMessageQueryStaleTime,
    queryFn: () => service.conversations.getDirectMessage(friend.userId),
    queryKey: ["directMessage", { userId: friend.userId }],
  });

  const isMounted = useIsMounted();
  const [showErrorSnack, setShowErrorSnack] = useSafeState(isMounted, false);

  const {
    error: createGroupChatError,
    mutate: createGroupChat,
    reset,
  } = useCreateGroupChat({
    onSuccess: (groupChatId) => {
      queryClient.invalidateQueries(["groupChats"]);
      history.push(routeToGroupChat(groupChatId));
    },
    onError: () => {
      setShowErrorSnack(true);
    },
  });

  return (
    <>
      {createGroupChatError && (
        <Snackbar
          autoHideDuration={5000}
          open={showErrorSnack}
          onClose={() => setShowErrorSnack(false)}
        >
          <Alert severity="error">{createGroupChatError.message}</Alert>
        </Snackbar>
      )}
      {isLoading ? (
        <CircularProgress />
      ) : groupChat ? (
        <Link to={routeToGroupChat(groupChat.groupChatId)}>
          <IconButton aria-label="Direct message">
            <EmailIcon />
          </IconButton>
        </Link>
      ) : (
        <IconButton
          aria-label="Direct message"
          onClick={() => {
            reset();
            createGroupChat({ title: "", users: [friend] });
          }}
        >
          <EmailIcon />
        </IconButton>
      )}
    </>
  );
}

function FriendList() {
  const { errors, isLoading, isError, data: friends } = useFriendList();

  return (
    <FriendTile
      title="Your friends"
      errorMessage={isError ? errors.join("\n") : null}
      isLoading={isLoading}
      hasData={!!friends?.length}
      noDataMessage="No friends available :("
    >
      {friends &&
        friends.map((friend) =>
          friend ? (
            <FriendSummaryView key={friend.userId} friend={friend}>
              <CurrentFriendAction friend={friend} />
            </FriendSummaryView>
          ) : null
        )}
    </FriendTile>
  );
}

export default FriendList;

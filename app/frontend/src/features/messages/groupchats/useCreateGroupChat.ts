import { Error as GrpcError } from "grpc-web";
import { User } from "pb/api_pb";
import { useMutation, UseMutationOptions } from "react-query";
import { service } from "service/index";

export interface CreateGroupChatFormData {
  title: string;
  users: User.AsObject[];
}

export default function useCreateGroupChat(
  options?: UseMutationOptions<number, GrpcError, CreateGroupChatFormData>
) {
  const createGroupChatMutationResult = useMutation<
    number,
    GrpcError,
    CreateGroupChatFormData
  >(
    ({ title, users }) => service.conversations.createGroupChat(title, users),
    options
  );

  return createGroupChatMutationResult;
}

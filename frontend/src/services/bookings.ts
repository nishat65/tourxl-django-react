import { axiosInstance } from "@/lib/utils";

export async function getBookings() {
  return await axiosInstance.get("bookings/");
}

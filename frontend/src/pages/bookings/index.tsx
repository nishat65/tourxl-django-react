import { useEffect } from "react";
import { useAppDispatch, useAppSelector } from "@/hooks/useStore";
import { fetchBookings } from "@/stores/bookings";

function Bookings() {
  const dispatch = useAppDispatch();
  const store = useAppSelector((state) => state.bookings);
  useEffect(() => {
    dispatch(fetchBookings())
      .unwrap()
      .then((data) => {
        console.log(data, "data");
      });
  }, []);
  console.log(store, "store");
  return <h1>Bookings</h1>;
}

export default Bookings;

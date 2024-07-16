import { useEffect } from "react";
import { useAppDispatch, useAppSelector } from "@/hooks/useStore";
import { fetchBookings } from "@/stores/bookings";

function Bookings() {
  const dispatch = useAppDispatch();
  const store = useAppSelector((state) => state.bookings);
  useEffect(() => {
    dispatch(fetchBookings());
  }, []);
  console.log(store.entities, store.loading, "store");
  return <h1>Bookings</h1>;
}

export default Bookings;

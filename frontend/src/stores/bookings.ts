import { createSlice, createAsyncThunk, AsyncThunk } from "@reduxjs/toolkit";
import { getBookings } from "@/services/bookings";
import { AxiosResponse } from "axios";
import { AsyncThunkConfig } from "node_modules/@reduxjs/toolkit/dist/createAsyncThunk";

export const fetchBookings: AsyncThunk<
  AxiosResponse<any, any>,
  void,
  AsyncThunkConfig
> = createAsyncThunk("bookings/fetchData", async () => {
  const response = await getBookings();
  return response.data;
});

export interface IBookings {
  entities: any;
  loading: "idle" | "pending" | "succeeded" | "failed";
}

const BookingsState: IBookings = {
  entities: [],
  loading: "idle",
};

const bookingsSlice = createSlice({
  initialState: BookingsState,
  name: "bookings",
  //   reducers: {
  //     setBookings: (state, action) => {
  //       state.entities = action.payload;
  //     },
  //     setBookingsLoading: (state, action) => {
  //       state.loading = action.payload;
  //     },
  //   },
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(fetchBookings.pending, (state, _) => {
      return { ...state, loading: "pending" };
    }),
      builder.addCase(fetchBookings.fulfilled, (state, action) => {
        return { ...state, loading: "succeeded", entities: action.payload };
      });
    builder.addCase(fetchBookings.rejected, (state, _) => {
      return { ...state, loading: "failed" };
    });
  },
});

// export const { setBookings, setBookingsLoading } = bookingsSlice.actions;

export default bookingsSlice.reducer;

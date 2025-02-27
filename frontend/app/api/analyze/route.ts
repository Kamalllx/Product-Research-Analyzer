import { NextResponse } from "next/server";

export async function POST(request: Request) {
  const { url, product } = await request.json();

  const flaskUrl = "http://localhost:5000/api/analyze-sync"; // Flask server URL

  const response = await fetch(flaskUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ url, product }),
  });

  const data = await response.json();
  return NextResponse.json(data);
}
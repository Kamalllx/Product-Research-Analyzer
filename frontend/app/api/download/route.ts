import { NextResponse } from "next/server";

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const url = searchParams.get("url");

  if (!url) {
    return NextResponse.json({ error: "URL is required" }, { status: 400 });
  }

  const response = await fetch(url);
  const blob = await response.blob();

  return new NextResponse(blob, {
    headers: {
      "Content-Disposition": `attachment; filename="paper.pdf"`,
      "Content-Type": "application/pdf",
    },
  });
}
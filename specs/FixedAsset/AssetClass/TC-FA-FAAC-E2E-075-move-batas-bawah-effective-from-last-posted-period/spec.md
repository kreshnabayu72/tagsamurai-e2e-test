---
id: TC-FA-FAAC-E2E-075-move-batas-bawah-effective-from-last-posted-period
title: "Move: Batas Bawah Effective From Akibat Accounting Period Closed dan Last Posted Period"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-200
  - TC-FA-FAAC-201
  - TC-FA-FAAC-202
coverage:
  web: automated
---

# Move: Batas Bawah Effective From Akibat Accounting Period Closed dan Last Posted Period

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE di hook `before` dan `after`): Asset Class Active 'Heavy Equipment' (HEAVY-EQ) dengan Asset Name "Wheel Loader" (4 aset aktif); Asset Class Active 'Machinery' (MACHINERY) sebagai tujuan; 'Vehicles' (VEHICLES) berstatus Active tersedia sebagai tujuan; 'Office Equipment (Legacy)' (OFFICE-OLD) berstatus Inactive (precondition TC, tidak diasersi). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE untuk mengatur per blok Accounting Period Closed dan Last Posted Period tiap Asset Class (langkah 3, 12, 21) dan memulihkannya di hook `after`; jam: bulan berjalan (M) dihitung pada zona waktu General Settings client (NC-11); kemampuan baca BE untuk Asset Class asal Asset Name.
- State global: periode akuntansi dan Last Posted Period berubah per blok; dipulihkan di hook `after`.
- Data uji per blok: TC-200 Accounting Period bulan M-2 Closed, Effective From = M-2 (mis. Aug 2026); TC-201 MACHINERY Last Posted Period M-3 tanpa Accounting Period Closed, Effective From = M-3 (mis. Jul 2026), batas bawah M-2 (mis. Aug 2026); TC-202 HEAVY-EQ Last Posted Period M-1 dan MACHINERY tanpa Last Posted Period, Effective From = M-1, batas bawah M (bulan berjalan).
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (seed spec lain ikut tampil), sehingga Class Code target dijangkau lewat Search kode (R-16), bukan lewat posisi baris di halaman 1.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `HEAVY-EQ`, tekan Enter
2. Klik link Class Code "HEAVY-EQ", lalu klik tab "Asset Names"

### TC-FA-FAAC-200: Effective From pada bulan Accounting Period berstatus Closed ditolak

3. Atur Accounting Period bulan M-2 berstatus Closed lewat fixture BE
4. Klik ikon ⋯ pada baris "Wheel Loader" lalu pilih "Move"
5. Pilih "Destination Asset Class" = "MACHINERY – Machinery"
6. Pilih Effective From = bulan M-2
7. Verifikasi caption error segera setelah memilih: "Period [MMM YYYY] is closed. Choose a later month." dengan [MMM YYYY] = bulan M-2 (mis. "Aug 2026")
8. Klik [Move]
9. Verifikasi Move tidak diproses: "Wheel Loader" tetap di Heavy Equipment
10. Verifikasi tidak ada toast
11. Klik [Cancel]

### TC-FA-FAAC-201: Effective From di bawah batas bawah akibat Last Posted Period Asset Class tujuan ditolak

12. Atur MACHINERY memiliki Last Posted Period M-3 dan tidak ada Accounting Period Closed lewat fixture BE
13. Klik ikon ⋯ pada baris "Wheel Loader" lalu pilih "Move"
14. Pilih "Destination Asset Class" = "MACHINERY – Machinery"
15. Pilih Effective From = bulan M-3
16. Verifikasi caption error segera setelah memilih: "Effective from must not be earlier than [MMM YYYY]" dengan [MMM YYYY] = bulan paling awal yang diizinkan M-2 (mis. "Aug 2026")
17. Klik [Move]
18. Verifikasi Move tidak diproses: "Wheel Loader" tetap di Heavy Equipment
19. Verifikasi tidak ada toast
20. Klik [Cancel]

### TC-FA-FAAC-202: Effective From di bawah batas bawah akibat Last Posted Period Asset Class asal ditolak

21. Atur HEAVY-EQ memiliki Last Posted Period M-1 dan MACHINERY tanpa Last Posted Period lewat fixture BE
22. Klik ikon ⋯ pada baris "Wheel Loader" lalu pilih "Move"
23. Pilih "Destination Asset Class" = "MACHINERY – Machinery"
24. Pilih Effective From = bulan M-1
25. Verifikasi caption error: "Effective from must not be earlier than [MMM YYYY]" dengan [MMM YYYY] = bulan berjalan (batas bawah dihitung dari Asset Class asal juga)
26. Klik [Move]
27. Verifikasi Move tidak diproses: "Wheel Loader" tetap di Heavy Equipment
28. Klik [Cancel]

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan: 200, 201, 202 (state periode tiap blok diatur ulang di langkah 3, 12, dan 21).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Class dan Asset Name seed dipakai apa adanya; spec tidak memindahkan Asset Name (setiap Move ditolak).
- Langkah penghubung (S-03): langkah 1, 2, 3, 11, 12, 20, 21, 28 (Search kode R-16, navigasi, pengaturan state periode, dan menutup dialog).
- Langkah 9, 18, dan 27 membaca Asset Class asal "Wheel Loader" lewat tab Asset Names HEAVY-EQ yang termuat.
- Temuan untuk QA: TC-200 memakai "Accounting Period bulan M-2 Closed" sebagai seed tanpa menyebut mekanismenya; spec menulisnya sebagai fixture BE yang disediakan tim FE/BE (NC-16).

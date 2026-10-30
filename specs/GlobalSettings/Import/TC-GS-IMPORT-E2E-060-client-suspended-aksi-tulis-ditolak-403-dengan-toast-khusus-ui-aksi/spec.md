---
id: TC-GS-IMPORT-E2E-060-client-suspended-aksi-tulis-ditolak-403-dengan-toast-khusus-ui-aksi
title: "Client Suspended: Aksi Tulis Ditolak 403 dengan Toast Khusus (UI), Aksi Baca Tetap Jalan; Permintaan Langsung dan Create Missing Options Ditolak 403"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-47
  - TC-GS-IMPORT-816
  - TC-GS-IMPORT-932
coverage:
  web: automated
---

# Client Suspended: Aksi Tulis Ditolak 403 dengan Toast Khusus (UI), Aksi Baca Tetap Jalan; Permintaan Langsung dan Create Missing Options Ditolak 403

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`) karena spec mengubah status Client; lihat `suite.md`.
- Klien HTTP: permintaan langsung ke server dengan token sesi akun yang diuji; token diperoleh lewat login API yang disediakan tim FE/BE.
- Akun: Total Control Client Suspended (Agus Wijaya) `totalControl_automated_qaTeam9@qwertysystem.net`, `Spectra.env.GS_CLIENTSUSP_TC_PASSWORD`; login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis yang disediakan tim FE/BE: fixture Admin Console untuk memulihkan Client Suspended ke Active dan men-Suspend kembali; skrip fixture untuk menyiapkan draft sebelum Suspend; mock layanan AI mode normal (D-40, tabel D-41 dan D-42).
- Data Dinamis (Client Suspended, disiapkan lewat skrip fixture sebelum client di-Suspend, oleh langkah 1 (TC-GS-IMPORT-47), langkah 13 (TC-GS-IMPORT-816), dan langkah 41 (TC-GS-IMPORT-932 varian 1)):
  - TC-GS-IMPORT-47: draft Brand 12 baris `pending` (isi seperti D-01: Acme Corp, Lenovo, Zebra Technologies, Honeywell, Dell, HP Inc, Canon, Epson, Brother, Logitech, Cisco, Asus); Sub-Tab Measurement tanpa draft; berkas `measurement-3.csv` (3 baris Measurement valid) dan `brand-12.csv`.
  - TC-GS-IMPORT-816: D-72 draft Brand 13 baris (baris #1-#12 seperti D-01, baris #13 `error` Brand Name 121 karakter nilai sumber Brand pertama tabel D-41 dengan badge saran AI `Samsung Electronics Indonesia`); D-73 draft User Login 1 baris `error` (Dedi Prakoso, Division `Logistik`); D-74 berkas sementara `brand-6.csv` (Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp) belum di-Confirm dan masih dalam masa simpan 60 menit; D-11/D-40 mock AI normal.
  - TC-GS-IMPORT-932 varian 1: D-91 draft User Login 1 baris `error` (Dedi Prakoso, Division `Engineering`, Access `Global Settings`, Shift `Lembur`); Custom Field `Shift` Dropdown opsi Pagi, Siang, Malam (Pre-setup).
- State global yang diubah dan dipulihkan: status Client Suspended (dipulihkan ke kondisi Pre-setup di hook `after`).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.

## Test Steps

### TC-GS-IMPORT-47: Aksi tulis lewat UI ditolak, aksi baca tetap jalan

1. Pulihkan Client Suspended ke Active; reset ke tanpa draft; buat draft TC-GS-IMPORT-47 (Brand 12 baris `pending` seperti D-01; Sub-Tab Measurement tanpa draft); Suspend kembali (fixture)
2. Muat ulang halaman Import > Brand
3. Verifikasi Staging Metric Cards Total Rows 12 dan Ready to Import 12
4. Verifikasi Pagination `Showing 1 - 10 of 12 items`
5. Klik sub-tab Measurement
6. Klik [Upload File]
7. Pilih berkas `measurement-3.csv` di file picker
8. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
9. Tutup toast "Changes can't be saved while this workspace is suspended or expired."
10. Klik sub-tab Brand
11. Klik [Import (12)]
12. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."

### TC-GS-IMPORT-816: Permintaan langsung ditolak 403 dan draft tidak berubah

13. Pulihkan Client Suspended ke Active; buat ulang draft D-72, D-73, dan berkas sementara D-74; Suspend kembali (fixture)
14. Kirim permintaan Confirm Mapping langsung ke server dengan token akun Total Control Client Suspended untuk berkas sementara D-74 pada Import Type Brand dengan pemetaan kolom `Brand Name` ke atribut Brand Name
15. Verifikasi permintaan ditolak server 403 Forbidden
16. Kirim permintaan Save sesi edit langsung ke server dengan token akun yang sama untuk baris `Lenovo` pada Import Type Brand dengan Brand Name diubah menjadi `Lenovo Baru`
17. Verifikasi permintaan ditolak server 403 Forbidden
18. Kirim permintaan Remove langsung ke server dengan token akun yang sama untuk baris `Zebra Technologies` pada Import Type Brand
19. Verifikasi permintaan ditolak server 403 Forbidden
20. Kirim permintaan Bulk Delete langsung ke server dengan token akun yang sama untuk baris `Honeywell` dan `Dell` pada Import Type Brand
21. Verifikasi permintaan ditolak server 403 Forbidden
22. Kirim permintaan Delete All Rows langsung ke server dengan token akun yang sama untuk kategori pesan `Brand Name: Max. 120 characters` pada Import Type Brand
23. Verifikasi permintaan ditolak server 403 Forbidden
24. Kirim permintaan AI Accept langsung ke server dengan token akun yang sama untuk sel Brand Name baris #13 pada Import Type Brand
25. Verifikasi permintaan ditolak server 403 Forbidden
26. Kirim permintaan AI Dismiss langsung ke server dengan token akun yang sama untuk sel Brand Name baris #13 pada Import Type Brand
27. Verifikasi permintaan ditolak server 403 Forbidden
28. Kirim permintaan Create Missing Divisions langsung ke server dengan token akun yang sama untuk baris dengan Division `Logistik` pada Import Type User Login
29. Verifikasi permintaan ditolak server 403 Forbidden
30. Muat ulang halaman Import > Brand
31. Verifikasi pembacaan Staging Table berhasil dan Staging Metric Cards: Total Rows 13 (Active), Ready to Import 12, Errors 1, Duplicates 0 (Disabled)
32. Verifikasi Error Summary Callout memuat "Brand Name: Max. 120 characters" dengan badge "1 row"
33. Verifikasi baris `Lenovo`, `Zebra Technologies`, `Honeywell`, dan `Dell` masih tampil
34. Verifikasi tidak ada baris `Lenovo Baru`
35. Pindah ke halaman 2 lewat Pagination
36. Verifikasi sel Brand Name baris #13 masih bernilai 121 karakter awal
37. Verifikasi badge saran "AI suggestion: 'Samsung Electronics Indonesia'?" disertai `[Accept]` dan `[Dismiss]` tampil
38. Buka Import > User Login
39. Verifikasi baris #1 berstatus `error`
40. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "1 row" beserta `[Create Missing Divisions]`

### TC-GS-IMPORT-932 (varian 1, Client Suspended): Create Missing Options langsung ditolak 403

41. Pulihkan Client Suspended ke Active; buat ulang draft D-91; Suspend kembali (fixture)
42. Kirim permintaan Create Missing Options untuk kategori "Shift: Invalid option" langsung ke server dengan token akun Total Control Client Suspended
43. Verifikasi permintaan ditolak server 403 Forbidden
44. Muat ulang halaman Import > User Login
45. Verifikasi baris #1 berstatus `error`
46. Verifikasi Error Summary Callout memuat "Shift: Invalid option" dengan badge "1 row"
47. Buka Global Settings > User > Custom Field dan buka Value Setting Shift
48. Verifikasi Value Setting Shift tetap seperti Pre-setup (tanpa `Lembur`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: state tenant (kelas h, prinsip 13h; write-lockdown Client Suspended). Permintaan langsung (langkah 14 sampai 29 dan 42) hanya mengasersi status respons dan state data (8b butir 1).
- Spec memuat 48 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (write-lockdown Client Suspended), tiap blok memakai draft yang dibuat ulang dan berdiri sendiri, dan blok TC-GS-IMPORT-816 berisi delapan permintaan homogen yang masing-masing mandiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 13, dan 41 (membuat draft dan status Client lewat fixture karena Client harus Active saat draft dibuat), langkah 2, 30, 38, 44 (muat ulang atau membuka halaman), langkah 9 (menutup toast sebelum toast berikutnya bertuliskan sama), langkah 35 (pindah ke halaman 2), langkah 47.
- Langkah 34 (absence `Lenovo Baru`) memakai baris `Lenovo` langkah 33 sebagai anchor positif; langkah 48 memakai Value Setting Shift Pre-setup yang terbaca sebagai anchor.
- Pembagian TC lintas spec: TC-GS-IMPORT-932 varian 2 (Client Expired) dijalankan di spec 061 sebagai langkah tambahan; id TC-GS-IMPORT-932 dicatat hanya di spec ini.
- Temuan untuk QA:
  - TC-GS-IMPORT-47 (draft Brand 12 baris) dan TC-GS-IMPORT-816 (draft Brand 13 baris D-72) memakai Sub-Tab Brand Client Suspended yang sama; draft dibuat ulang antar blok.
  - TC-GS-IMPORT-816 dan 932 mensyaratkan draft dibuat sebelum client di-Suspend; spec menambahkan langkah fixture pemulihan dan Suspend ulang sebagai langkah penghubung.
  - TC-GS-IMPORT-932 tidak menyebut pembukaan Sub-Tab User Login selain "Muat ulang halaman Import > User Login"; spec mengikuti langkah TC.

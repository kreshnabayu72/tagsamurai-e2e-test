---
id: TC-GS-IMPORT-E2E-061-client-expired-discard-draft-ditolak-403-dengan-toast-khusus-confirm
title: "Client Expired: Discard Draft Ditolak 403 dengan Toast Khusus; Permintaan Langsung dan Create Missing Options Ditolak 403"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-48
  - TC-GS-IMPORT-817
coverage:
  web: automated
---

# Client Expired: Discard Draft Ditolak 403 dengan Toast Khusus; Permintaan Langsung dan Create Missing Options Ditolak 403

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`) karena spec mengubah status Client; lihat `suite.md`.
- Klien HTTP: permintaan langsung ke server dengan token sesi akun yang diuji; token diperoleh lewat login API yang disediakan tim FE/BE.
- Akun: Total Control Client Expired (Citra Maharani) `totalControl_automated_qaTeam11@qwertysystem.net`, `Spectra.env.GS_CLIENTEXP_TC_PASSWORD`; login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis yang disediakan tim FE/BE: fixture Admin Console untuk memulihkan Client Expired ke Active dan meng-Expire kembali; skrip fixture untuk menyiapkan draft sebelum Expire; mock layanan AI mode normal (D-40, tabel D-41 dan D-42); hook umur draft D-76.
- Data Dinamis (Client Expired, disiapkan lewat skrip fixture sebelum client di-Expire, oleh langkah 1 (TC-GS-IMPORT-48), langkah 8 (TC-GS-IMPORT-817), dan langkah 36 (TC-GS-IMPORT-932 varian 2)):
  - TC-GS-IMPORT-48: draft Brand 12 baris `pending` (isi seperti D-01) dengan D-76 varian 1 (`created_at` dimundurkan 25 jam, hanya seed backdate) sehingga Unsaved Banner tampil.
  - TC-GS-IMPORT-817: D-72 draft Brand 13 baris (baris #1-#12 seperti D-01, baris #13 `error` Brand Name 121 karakter nilai sumber Brand pertama tabel D-41 dengan badge saran AI `Samsung Electronics Indonesia`); D-73 draft User Login 1 baris `error` (Dedi Prakoso, Division `Logistik`); D-74 berkas sementara `brand-6.csv` (Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp) belum di-Confirm dan masih dalam masa simpan 60 menit.
  - TC-GS-IMPORT-932 varian 2: D-91 draft User Login 1 baris `error` (Dedi Prakoso, Division `Engineering`, Access `Global Settings`, Shift `Lembur`); master data seperti Client A dan Custom Field `Shift` Dropdown opsi Pagi, Siang, Malam pada Client Expired disiapkan seperti D-75 sebelum Expire.
- State global yang diubah dan dipulihkan: status Client Expired (dipulihkan ke kondisi Pre-setup di hook `after`).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.

## Test Steps

### TC-GS-IMPORT-48: Discard Draft ditolak 403 dengan toast khusus

1. Pulihkan Client Expired ke Active; reset ke tanpa draft; buat draft TC-GS-IMPORT-48 (Brand 12 baris `pending`, isi seperti D-01) dengan D-76 varian 1 (`created_at` dimundurkan 25 jam); Expire kembali (fixture)
2. Muat ulang halaman Import > Brand
3. Klik [Discard] pada Unsaved Banner
4. Klik [Discard Draft] pada dialog Discard Draft
5. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
6. Muat ulang halaman Import
7. Verifikasi Staging Table tetap menampilkan 12 baris draft

### TC-GS-IMPORT-817: Permintaan langsung ditolak 403 dan draft tidak berubah

8. Pulihkan Client Expired ke Active; buat ulang draft D-72, D-73, dan berkas sementara D-74; Expire kembali (fixture)
9. Kirim permintaan Confirm Mapping langsung ke server dengan token akun Total Control Client Expired untuk berkas sementara D-74 pada Import Type Brand dengan pemetaan kolom `Brand Name` ke atribut Brand Name
10. Verifikasi permintaan ditolak server 403 Forbidden
11. Kirim permintaan Save sesi edit langsung ke server dengan token akun yang sama untuk baris `Lenovo` pada Import Type Brand dengan Brand Name diubah menjadi `Lenovo Baru`
12. Verifikasi permintaan ditolak server 403 Forbidden
13. Kirim permintaan Remove langsung ke server dengan token akun yang sama untuk baris `Zebra Technologies` pada Import Type Brand
14. Verifikasi permintaan ditolak server 403 Forbidden
15. Kirim permintaan Bulk Delete langsung ke server dengan token akun yang sama untuk baris `Honeywell` dan `Dell` pada Import Type Brand
16. Verifikasi permintaan ditolak server 403 Forbidden
17. Kirim permintaan Delete All Rows langsung ke server dengan token akun yang sama untuk kategori pesan `Brand Name: Max. 120 characters` pada Import Type Brand
18. Verifikasi permintaan ditolak server 403 Forbidden
19. Kirim permintaan AI Accept langsung ke server dengan token akun yang sama untuk sel Brand Name baris #13 pada Import Type Brand
20. Verifikasi permintaan ditolak server 403 Forbidden
21. Kirim permintaan AI Dismiss langsung ke server dengan token akun yang sama untuk sel Brand Name baris #13 pada Import Type Brand
22. Verifikasi permintaan ditolak server 403 Forbidden
23. Kirim permintaan Create Missing Divisions langsung ke server dengan token akun yang sama untuk baris dengan Division `Logistik` pada Import Type User Login
24. Verifikasi permintaan ditolak server 403 Forbidden
25. Muat ulang halaman Import > Brand
26. Verifikasi pembacaan Staging Table berhasil dan Staging Metric Cards: Total Rows 13 (Active), Ready to Import 12, Errors 1, Duplicates 0 (Disabled)
27. Verifikasi Error Summary Callout memuat "Brand Name: Max. 120 characters" dengan badge "1 row"
28. Verifikasi baris `Lenovo`, `Zebra Technologies`, `Honeywell`, dan `Dell` masih tampil
29. Verifikasi tidak ada baris `Lenovo Baru`
30. Pindah ke halaman 2 lewat Pagination
31. Verifikasi sel Brand Name baris #13 masih bernilai 121 karakter awal
32. Verifikasi badge saran "AI suggestion: 'Samsung Electronics Indonesia'?" disertai `[Accept]` dan `[Dismiss]` tampil
33. Buka Import > User Login
34. Verifikasi baris #1 berstatus `error`
35. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "1 row" beserta `[Create Missing Divisions]`

### TC-GS-IMPORT-932 (varian 2, Client Expired): Create Missing Options langsung ditolak 403

36. Pulihkan Client Expired ke Active; buat ulang draft D-91; Expire kembali (fixture)
37. Kirim permintaan Create Missing Options untuk kategori "Shift: Invalid option" langsung ke server dengan token akun Total Control Client Expired
38. Verifikasi permintaan ditolak server 403 Forbidden
39. Muat ulang halaman Import > User Login
40. Verifikasi baris #1 berstatus `error`
41. Verifikasi Error Summary Callout memuat "Shift: Invalid option" dengan badge "1 row"
42. Buka Global Settings > User > Custom Field dan buka Value Setting Shift
43. Verifikasi Value Setting Shift tetap seperti Pre-setup (tanpa `Lembur`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: state tenant (kelas h, prinsip 13h; write-lockdown Client Expired). Permintaan langsung hanya mengasersi status respons dan state data (8b butir 1).
- Spec memuat 43 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (write-lockdown Client Expired), tiap blok memakai draft yang dibuat ulang dan berdiri sendiri, dan blok TC-GS-IMPORT-817 berisi delapan permintaan homogen yang masing-masing mandiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 8, dan 36 (membuat draft dan status Client lewat fixture), langkah 2, 6, 25, 39 (muat ulang halaman), langkah 30 (pindah ke halaman 2), langkah 33 dan 42 (membuka halaman).
- Langkah 29 (absence `Lenovo Baru`) memakai baris `Lenovo` langkah 28 sebagai anchor; langkah 43 memakai Value Setting Shift Pre-setup yang terbaca sebagai anchor.
- Pembagian TC lintas spec: TC-GS-IMPORT-932 varian 2 (Client Expired) dijalankan di spec ini sebagai langkah tambahan; id TC-GS-IMPORT-932 dicatat di `sourceTc` spec 060 (varian 1, Client Suspended).
- Temuan untuk QA:
  - TC-GS-IMPORT-932 varian 2 tidak merujuk D-75 meski Pre-setup Client Expired menyatakan master data hanya bila disiapkan oleh D-75; spec memakai Division `Engineering` dan Custom Field `Shift` dari D-75 sebagai prasyarat D-91.
  - TC-GS-IMPORT-48 Post Condition ("Draft tidak berubah") setara dengan Expected b.

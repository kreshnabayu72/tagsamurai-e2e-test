---
id: TC-FA-FAAC-E2E-121-sort-3-state-active-accounts-last-updated
title: "Sort 3-State Tabel Asset Class: Active, Accounts, Last Updated, Satu Kolom Sort Aktif, dan Kolom Tanpa Ikon Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-390
  - TC-FA-FAAC-391
  - TC-FA-FAAC-392
  - TC-FA-FAAC-393
  - TC-FA-FAAC-394
coverage:
  web: automated
---

# Sort 3-State Tabel Asset Class: Active, Accounts, Last Updated, Satu Kolom Sort Aktif, dan Kolom Tanpa Ikon Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Kondisi Accounts: IT-EQ memiliki satu akun Inactive; MACHINERY dan LAND belum lengkap. Last Updated (waktu entri Changelog terbaru): HEAVY-EQ = 28 Oct 2026 (14:30); STORAGE = 27 Oct 2026 (01:00); IT-EQ = 1 Oct 2026 (00:05); MACHINERY = 30 Sep 2026 (16:20); OFFICE-NEW = 23 Sep 2026 (10:40); OFFICE-OLD = 22 Sep 2026 (14:05); VEHICLES = 15 Sep 2026 (11:30); BLDG dan LAND = 5 Jan 2026 (belum ada entri Changelog: waktu dibuat, tanggal dan jam sama). Assets: HEAVY-EQ 40, IT-EQ 62, LAND 4, MACHINERY 7, VEHICLES 18, kelas lain 0. Seed disediakan tim FE/BE (lihat `suite.md`).
- Tabel "Kolom yang diuji" (parameter langkah 3 sampai 8; urutan relatif awal baris contoh pada Class Code A-Z: BLDG, HEAVY-EQ, IT-EQ, LAND, MACHINERY, OFFICE-NEW, OFFICE-OLD, STORAGE, VEHICLES):

| Kolom | TC | Klik 1 (naik) | Klik 2 (turun) |
|---|---|---|---|
| Active | TC-FA-FAAC-390 | Active First: baris Active tampil lebih dulu dan OFFICE-OLD (Inactive) paling akhir | Inactive First: OFFICE-OLD paling atas |
| Accounts | TC-FA-FAAC-391 | belum lengkap (LAND, MACHINERY), lalu ada akun Inactive (IT-EQ), lalu lengkap (BLDG, HEAVY-EQ, OFFICE-NEW, OFFICE-OLD, STORAGE, VEHICLES) | lengkap (BLDG, HEAVY-EQ, OFFICE-NEW, OFFICE-OLD, STORAGE, VEHICLES), lalu IT-EQ, lalu LAND, MACHINERY |
| Last Updated | TC-FA-FAAC-392 | Oldest First: BLDG, LAND, VEHICLES, OFFICE-OLD, OFFICE-NEW, MACHINERY, IT-EQ, STORAGE, HEAVY-EQ | Newest First: HEAVY-EQ, STORAGE, IT-EQ, MACHINERY, OFFICE-NEW, OFFICE-OLD, VEHICLES, lalu BLDG dan LAND (waktu sama, urut Class Code A-Z) |

- State yang diubah spec: konfigurasi kolom tabel (kolom Last Updated ditampilkan oleh langkah 1 dan 2 lalu disembunyikan oleh langkah 19 dan 20). Pemulihan cadangan di hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; lihat `suite.md`).
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (sembilan kelas contoh ditambah seed lain seperti `B-*`, `PMP-01`, `B-PAGE01` sampai `B-PAGE11`, `TEMP-EQ`, dan seed spec lain), sehingga sembilan kelas contoh tidak dijamin berada bersama pada halaman 1 dan baris seed lain dapat menyela atau ikut tampil. Asersi spec ini dibatasi pada keanggotaan dan urutan RELATIF antar baris contoh (atau pada baris yang dikenali lewat Search kode); baris seed lain tidak diasersi.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Persiapan (TC-FA-FAAC-392 langkah 1)

1. Aktifkan kolom Last Updated lewat Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`, centang Last Updated)
2. Klik `[Save]`

### Sort 3-state per kolom (TC-FA-FAAC-390, 391, 392)

Untuk setiap baris tabel "Kolom yang diuji" pada Prerequisites, dari Active sampai Last Updated (langkah 3 sampai 8):

3. Klik header kolom satu kali, lalu telusuri seluruh halaman tabel dari halaman 1 sampai halaman terakhir (Next)
4. Verifikasi urutan relatif baris contoh naik sesuai kolom "Klik 1 (naik)" pada baris tabel kolom itu
5. Klik header kolom kedua kali, lalu telusuri seluruh halaman tabel dari halaman 1 sampai halaman terakhir (Next)
6. Verifikasi urutan relatif baris contoh turun sesuai kolom "Klik 2 (turun)" pada baris tabel kolom itu
7. Klik header kolom ketiga kali, lalu telusuri seluruh halaman tabel dari halaman 1 sampai halaman terakhir (Next)
8. Verifikasi sort netral kembali ke Class Code A-Z dengan urutan relatif baris contoh: BLDG, HEAVY-EQ, IT-EQ, LAND, MACHINERY, OFFICE-NEW, OFFICE-OLD, STORAGE, VEHICLES

### TC-FA-FAAC-393: Hanya satu kolom sort aktif pada satu waktu

9. Klik header Class Name satu kali
10. Klik header Assets satu kali
11. Verifikasi indikator sort Class Name hilang dan hanya Assets yang aktif naik
12. Verifikasi tabel diurutkan menurut Assets
13. Klik header Assets dua kali lagi (sort kembali netral)

### TC-FA-FAAC-394: Kolom Checkbox dan Column Visibility tidak memiliki ikon sort

14. Verifikasi kolom Checkbox dan kolom Column Visibility (`⋯`) tidak memiliki ikon sort
15. Klik header kolom Column Visibility (`⋯`)
16. Verifikasi panel Column Visibility terbuka
17. Verifikasi urutan baris tabel tidak berubah (header `⋯` tidak mengurutkan tabel)
18. Tutup panel Column Visibility dengan klik di luar panel

### Pemulihan

19. Sembunyikan kembali kolom Last Updated lewat Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`, hilangkan centang Last Updated)
20. Klik `[Save]`

## Notes

- Langkah 3 sampai 8 diulang untuk tiga baris tabel Prerequisites (bagian 8b butir 7); `Verifikasi` tetap satu per klausa: naik, turun, netral per kolom. Pembagian TC lintas baris tabel: TC-FA-FAAC-390 (Active), TC-FA-FAAC-391 (Accounts), TC-FA-FAAC-392 (Last Updated). Dengan ekspansi spec ini berjumlah 32 langkah.
- Penelusuran seluruh halaman (S-14) menjadi bagian langkah 3, 5, dan 7: tabel memuat lebih dari 25 baris sehingga baris contoh tersebar di beberapa halaman dan seed lain dapat menyela; asersi `Verifikasi` hanya pada urutan relatif baris contoh.
- Langkah penghubung (S-03): langkah 13 (mengembalikan sort ke netral sebelum TC-FA-FAAC-394, S-09), langkah 18 (menutup panel Column Visibility), langkah 19 dan 20 (memulihkan konfigurasi kolom, S-09).
- Langkah 17 mengasersi butir Expected "bukan mengurutkan tabel" TC-FA-FAAC-394 dengan membandingkan urutan baris sebelum dan sesudah klik header `⋯`; urutan sebelum klik adalah Class Code A-Z (langkah 13).
- Nama literal Pre-setup (sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan urutan relatif antar baris contoh, dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA: tidak ada.

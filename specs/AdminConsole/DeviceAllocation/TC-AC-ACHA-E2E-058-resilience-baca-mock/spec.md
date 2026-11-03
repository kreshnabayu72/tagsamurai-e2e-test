---
id: TC-AC-ACHA-E2E-058-resilience-baca-mock
title: "Resilience Baca (Mock): Error Load pada Tabel List, Panel Stock Balance, Modal Allocation Log, dan Kegagalan Download"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHA-8
  - TC-AC-ACHA-25
  - TC-AC-ACHA-34
  - TC-AC-ACHA-364
coverage:
  web: automated
---

# Resilience Baca (Mock): Error Load pada Tabel List, Panel Stock Balance, Modal Allocation Log, dan Kegagalan Download

## Prerequisites

- Mode: mock
- Kelas harness b (fault injection / resilience baca). Seluruh API di-mock (dijalankan tim FE sebagai integration test, tanpa backend nyata); spec hanya mengasersi perilaku FE atas respons mock (konvensi bagian 6, resilience `Mode: mock`).
- Kebutuhan mock (`Spectra.intercept()` atau mock server FE): respons normal untuk data tabel List (Seed 30 alokasi Pre-setup #48 dengan 10 baris pada halaman pertama), data panel Stock Balance, data Allocation Log transaksi `HALC-20260901-00001`, dan berkas Download; tiap TC memaksa satu respons menjadi server error 500 lalu memulihkannya:
  - TC-AC-ACHA-8: respons `POST /v2/enterprise-management/device-allocations/list` 500, lalu respons normal sesudah intercept dilepas;
  - TC-AC-ACHA-25: respons `GET /v2/enterprise-management/device-allocations/allocated-quota` 500, lalu respons normal;
  - TC-AC-ACHA-34: respons `GET /v2/analytics-reporting/device-allocations/{id}/logs` 500, lalu respons normal;
  - TC-AC-ACHA-364: respons `POST /v2/enterprise-management/device-allocations/export` 500.
  Intercept dilepas segera setelah pemicu selesai dan dipulihkan di hook `after` bila spec gagal di tengah.
- Daftar endpoint yang di-mock (S-13, R-15; dari `openapi.yaml` dan `low-level-design.md` modul):
  - List: `POST /v2/enterprise-management/device-allocations/list` (TC-AC-ACHA-8);
  - panel Stock Balance (Allocated quota): `GET /v2/enterprise-management/device-allocations/allocated-quota` (TC-AC-ACHA-25);
  - Allocation Log: `GET /v2/analytics-reporting/device-allocations/{id}/logs` (TC-AC-ACHA-34);
  - Download: `POST /v2/enterprise-management/device-allocations/export` (TC-AC-ACHA-364).
  API pendukung di luar sumber modul (identitas pengguna, menu, flag Guided Tooltip `guided_tooltip_seen_<page_key>`, Setup Column) disediakan tim FE; tidak ada SSE stream yang diketahui dari sumber modul.
- Identitas pengguna (mock, disediakan tim FE; tidak ada login backend): Total Control Principal (Pre-setup #21, Admin Pratama) untuk TC-AC-ACHA-8, 34, 364 dan Total Control Distributor (Pre-setup #27, Hendra Wibowo) untuk TC-AC-ACHA-25; password tidak dipakai pada mode mock.
- Hook `before` spec ini memasang mock identitas, menu, dan flag Guided Tooltip untuk akun yang dipakai; halaman dibuka hook `beforeEach` suite. Hook `after` melepas semua intercept.
- Tunggu waktu nyata: 10 detik pada TC-AC-ACHA-364 untuk memastikan toast error persisten tetap tampil (jeda pendek, bagian 6 konvensi).
- Suite berjalan serial (`parallel: false`).
- Data seed mock: Seed List 30 baris dan baris `HALC-20260901-00001` (Pre-setup #48) disediakan tim FE sebagai fixture respons mock (`Fixture.AdminConsoleDeviceAllocation`); tidak ada seeding backend dan tidak ada Data Dinamis.
- Readback respons mock: Seed List (`HALC-20260901-00001` dan baris lain Pre-setup #48) dipakai sebagai isi respons mock; tidak ada asersi readback di luar Expected TC (bagian 6 konvensi).

## Test Steps

### TC-AC-ACHA-8: State Error Load pada tabel List dan pemulihan lewat Try Again

1. Atur mock respons data tabel List menjadi server error 500
2. Buka halaman Allocation > Device Allocation
3. Verifikasi tabel menampilkan teks "Unable to load this data."
4. Verifikasi tabel menampilkan tombol `[Try Again]`
5. Lepas intercept data tabel List sehingga respons mock normal
6. Klik `[Try Again]`
7. Verifikasi 10 baris tampil pada tabel
8. Verifikasi teks error "Unable to load this data." hilang

### TC-AC-ACHA-34: State Error Load pada modal Allocation Log

9. Atur mock respons data Allocation Log menjadi server error 500
10. Klik Allocation ID `HALC-20260901-00001`
11. Verifikasi modal Allocation Log menampilkan teks "Unable to load this data."
12. Verifikasi modal Allocation Log menampilkan tombol `[Try Again]`
13. Lepas intercept data Allocation Log sehingga respons mock normal
14. Klik `[Try Again]`
15. Verifikasi daftar log tampil pada modal Allocation Log
16. Tutup modal Allocation Log dengan `[×]`

### TC-AC-ACHA-364: Kegagalan Download

17. Atur mock respons Download menjadi server error 500
18. Klik Download lalu `Download as CSV`
19. Tunggu 10 detik tanpa menutup toast
20. Verifikasi toast error "Error, failed to download Device-Allocation." tanpa extension
21. Verifikasi toast tidak hilang otomatis sampai di-dismiss: toast masih tampil sesudah 10 detik
22. Lepas intercept respons Download
23. Dismiss toast secara manual

### Ganti identitas ke Total Control Distributor (mock)

24. Ganti mock identitas pengguna menjadi Total Control Distributor (Pre-setup #27), lalu muat ulang halaman Allocation > Device Allocation

### TC-AC-ACHA-25: State Error Load per panel dan pemulihan

25. Atur mock respons data panel Stock Balance menjadi server error 500
26. Muat ulang halaman Allocation > Device Allocation
27. Verifikasi panel menampilkan teks "Unable to load this data." pada panel itu
28. Verifikasi panel menampilkan tombol `[Try Again]` pada panel itu
29. Verifikasi tabel List tetap tampil normal
30. Lepas intercept data panel sehingga respons mock normal
31. Klik `[Try Again]` pada panel
32. Verifikasi panel menampilkan kuota normal

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (Section 1b, 1d, 1e, 4a-7). Mode mock: seluruh TC di spec ini hanya mengasersi perilaku FE atas respons mock; TC kegagalan tulis (500, timeout, Approve atau Reject gagal) ada di spec 059 (`FE+BE`).
- Penyimpangan urutan: TC-AC-ACHA-25 ditaruh terakhir karena memakai identitas Total Control Distributor, sedangkan TC-AC-ACHA-8, 34, 364 memakai Total Control Principal; urutan di antara ketiga TC itu mengikuti nomor TC dengan TC-AC-ACHA-34 sebelum TC-AC-ACHA-364.
- Langkah penghubung (S-03): langkah memasang dan melepas intercept (S-09), langkah tunggu 10 detik (jeda nyata pendek, bagian 6), tutup modal Allocation Log, dismiss toast, ganti identitas mock (S-07, diganti dengan langkah eksplisit).
- Temuan untuk QA:
  - TC-AC-ACHA-25 b menyebut "panel menampilkan kuota normal" tanpa nilai kuota; spec tidak mengasersi angka. Panel Stock Balance tersedia untuk Distributor (TC memakai Pre-setup #27) tetapi precondition tidak menyebut nilai respons mock panel.
  - TC-AC-ACHA-8 a menyebut "bukan empty state" tanpa teks empty state yang dimaksud; spec mengasersi teks error dan tombol saja.
  - TC-AC-ACHA-364 menyebut toast "tidak hilang otomatis sampai di-dismiss" tanpa durasi pengamatan; spec memakai 10 detik (pilihan spec).
  - Catatan TC yang menyatakan modul tidak punya API atau LLD tidak sesuai: `openapi.yaml` dan `low-level-design.md` modul ada dan memuat endpoint List, allocated-quota, Allocation Log, dan export; spec memakai endpoint dari kedua berkas itu. Catatan TC perlu dikoreksi pemilik TC.
  - TC-AC-ACHA-8, 25, 34, 364 memakai kolom "Respons ... dipaksa 500" tanpa mengidentifikasi endpoint; spec mengisinya dari `openapi.yaml` dan `low-level-design.md`.
  - Post Condition TC-AC-ACHA-8, 25, 34, 364 ("-") tidak ada.

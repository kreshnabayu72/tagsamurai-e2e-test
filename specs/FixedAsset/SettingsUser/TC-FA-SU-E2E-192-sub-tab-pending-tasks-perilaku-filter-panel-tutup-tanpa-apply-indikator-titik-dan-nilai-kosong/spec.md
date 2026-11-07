---
id: TC-FA-SU-E2E-192-sub-tab-pending-tasks-perilaku-filter-panel-tutup-tanpa-apply-indikator-titik-dan-nilai-kosong
title: "Sub-tab Pending Tasks: Perilaku Filter Panel (Tutup Tanpa Apply, Indikator Titik, dan Nilai Kosong)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-522
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Perilaku Filter Panel (Tutup Tanpa Apply, Indikator Titik, dan Nilai Kosong)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Responsibilities (#25): pengguna target Budi Santoso dengan 5 baris Sub-tab Pending Tasks (`BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`). Nilai kolom tiap baris mengikuti Pre-setup #25; asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11).
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; perubahan tampilan (Search, Filter, Sort, Column Visibility) dipulihkan oleh langkah penghubung spec.
- Urutan default (Request Date ascending): `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`.

## Test Steps

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks

### TC-FA-SU-522: Perilaku Filter Panel: tutup tanpa Apply, indikator titik, dan nilai kosong

3. Klik icon Filter
4. Buka dropdown Transaction lalu centang `Assignment` tanpa `[Apply]`
5. Klik di luar Filter Panel
6. Klik icon Filter
7. Verifikasi field Transaction menampilkan nilai ter-Apply terakhir (kosong, tanpa chip)
8. Verifikasi tabel tidak berubah (`BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`)
9. Buka dropdown Transaction lalu centang `Assignment`
10. Klik `[Apply]`
11. Verifikasi ikon Filter menampilkan badge titik dengan panel terbuka
12. Klik icon Filter
13. Verifikasi ikon Filter menampilkan badge titik dengan panel tertutup
14. Klik icon Filter
15. Klik `[Clear Field]` pada field Transaction
16. Klik `[Apply]`
17. Verifikasi badge titik pada ikon Filter hilang
18. Buka dropdown Group
19. Verifikasi dropdown Group memuat opsi data (`Branch Surabaya`, `Finance & Accounting`, `General Affairs`, `IT Infrastructure`, `Logistics Warehouse`) tanpa opsi untuk nilai kosong
20. Buka dropdown Transaction lalu centang `Assignment`
21. Klik `[Apply]`
22. Klik header kolom Actions (⋯), lalu hilangkan centang Transaction
23. Klik icon Filter
24. Verifikasi field Transaction masih ada pada Filter Panel
25. Verifikasi filter Transaction `Assignment` ter-Apply tetap berlaku (`ASG-20260715-0045`, `ASG-20260718-0067`)
26. Klik header kolom Actions (⋯), lalu centang kembali Transaction

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Budi Santoso dan Filter Panel; mengembalikan kolom Transaction (S-09).
- Langkah penghubung tambahan (S-03): langkah 1 (Ketik Search `Budi Santoso`, tekan Enter sebelum membuka Detail, supaya spec tidak mengandalkan posisi baris pada User List 25 pengguna 3 halaman, R-16, bagian 8b butir 13).
- TC-FA-SU-520 dan TC-FA-SU-521 ada di spec 175.
- Jumlah langkah: 26 tertulis, 26 dengan ekspansi iterasi.
- Temuan untuk QA:
  - TC-FA-SU-522 Expected c: "memilih opsi apa pun menyaring keluar baris yang nilainya kosong" tidak teramati karena fixture Pre-setup #25 tidak memuat baris dengan nilai kosong pada kolom filter; spec mengasersi dropdown Group tanpa opsi nilai kosong.

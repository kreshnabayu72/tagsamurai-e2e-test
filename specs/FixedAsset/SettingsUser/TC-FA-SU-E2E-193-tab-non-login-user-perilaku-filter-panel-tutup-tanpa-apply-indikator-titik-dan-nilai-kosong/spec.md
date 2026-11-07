---
id: TC-FA-SU-E2E-193-tab-non-login-user-perilaku-filter-panel-tutup-tanpa-apply-indikator-titik-dan-nilai-kosong
title: "Tab Non-Login User: Perilaku Filter Panel (Tutup Tanpa Apply, Indikator Titik, dan Nilai Kosong)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-557
coverage:
  web: automated
---

# Tab Non-Login User: Perilaku Filter Panel (Tutup Tanpa Apply, Indikator Titik, dan Nilai Kosong)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Non-Login User (#26): pengguna target Budi Santoso dengan 5 Non-Login User (`Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`; `Printer Lantai 5` Inactive). Asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11); kolom tanpa nilai distinct dicatat di Temuan untuk QA.
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; perubahan tampilan (Search, Filter, Sort, Column Visibility) dipulihkan oleh langkah penghubung spec.
- Urutan default (Name ascending): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`.

## Test Steps

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail Budi Santoso > Tab Non-Login User

### TC-FA-SU-557: Perilaku Filter Panel: tutup tanpa Apply, indikator titik, dan nilai kosong

3. Klik icon Filter
4. Buka dropdown Division lalu centang `Facility` tanpa `[Apply]`
5. Klik di luar Filter Panel
6. Klik icon Filter
7. Verifikasi field Division menampilkan nilai ter-Apply terakhir (kosong, tanpa chip)
8. Verifikasi tabel tidak berubah (`Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`)
9. Buka dropdown Division lalu centang `Facility`
10. Klik `[Apply]`
11. Verifikasi ikon Filter menampilkan badge titik dengan panel terbuka
12. Klik icon Filter
13. Verifikasi ikon Filter menampilkan badge titik dengan panel tertutup
14. Klik icon Filter
15. Klik `[Clear Field]` pada field Division
16. Klik `[Apply]`
17. Verifikasi badge titik pada ikon Filter hilang
18. Buka dropdown Division
19. Verifikasi dropdown Division memuat opsi data (`Facility`, `General Affairs`, `Logistics`, `Logistics Warehouse`)
20. Buka dropdown Position
21. Verifikasi dropdown Position tidak memuat opsi data (tidak ada opsi untuk nilai kosong)
22. Buka dropdown Division lalu centang `Facility`
23. Klik `[Apply]`
24. Klik header kolom Actions (⋯), lalu hilangkan centang Division
25. Klik icon Filter
26. Verifikasi field Division masih ada pada Filter Panel
27. Verifikasi filter Division `Facility` ter-Apply tetap berlaku (hasil `Ruang Meeting Anggrek`)
28. Klik header kolom Actions (⋯), lalu centang kembali Division

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Budi Santoso dan Filter Panel; mengembalikan kolom Division (S-09).
- Langkah penghubung tambahan (S-03): langkah 1 (Ketik Search `Budi Santoso`, tekan Enter sebelum membuka Detail, supaya spec tidak mengandalkan posisi baris pada User List 25 pengguna 3 halaman, R-16, bagian 8b butir 13).
- TC-FA-SU-555 dan TC-FA-SU-556 ada di spec 186.
- Jumlah langkah: 28 tertulis, 28 dengan ekspansi iterasi.
- Temuan untuk QA:
  - Langkah 18 sampai 19 (membuka dan memverifikasi opsi dropdown Division) ditambahkan spec sebagai anchor positif sebelum asersi absence opsi dropdown Position (bagian 8b butir 2); TC tidak menyebutnya.
  - TC-FA-SU-557 Expected c: dropdown Position tidak memuat opsi (seluruh nilai kosong, TC-FA-SU-552) dan "memilih opsi apa pun menyaring keluar baris yang nilainya kosong" tidak teramati karena tidak ada opsi untuk kolom bernilai kosong; spec mengasersi dropdown Position tanpa opsi.

---
id: TC-FA-FAAC-E2E-065-edit-depreciation-akun-dan-status-inactive
title: "Edit Depreciation, Accounts, dan Asset Class Inactive pada Asset Class yang Belum Dipakai Aset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-176
  - TC-FA-FAAC-177
  - TC-FA-FAAC-178
coverage:
  web: automated
---

# Edit Depreciation, Accounts, dan Asset Class Inactive pada Asset Class yang Belum Dipakai Aset

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE di hook `before` dan `after`): Asset Class `B-DB` (belum dipakai aset; Method Declining Balance, Useful Life 48, Declining Rate 50%/yr); Asset Class `B-ANCHOR` (Last Exported Period kosong; Asset Cost awal sesuai seed); Asset Class `B-INACT` (Inactive). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Data uji: Useful Life 48 menjadi 60; Asset Cost "11002 – Machinery Cost Alt" (akun Active di Chart of Accounts, disediakan seed); Class Name "Inactive Renamed".
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan Asset Class lewat fixture BE; kemampuan baca BE untuk jumlah versi Asset Class.
- State global: tidak ada yang diubah selain Asset Class di atas; dipulihkan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-176: Edit tab Depreciation pada Asset Class yang belum dipakai aset tersimpan langsung

1. Klik link Class Code "B-DB" di tabel
2. Klik tab "Depreciation" dan ubah Useful Life dari 48 menjadi 60
3. Klik "Save"
4. Verifikasi muncul toast sukses: "Success, asset class has been updated."
5. Verifikasi tidak muncul Dialog Apply Changes
6. Verifikasi baris B-DB menampilkan Commercial "Declining Balance · 5 yrs · 50%/yr"
7. Verifikasi perubahan berlaku langsung tanpa Effective From dan tanpa pratinjau dampak
8. Klik link Class Code "B-DB" di tabel
9. Verifikasi Alert versi Scheduled tidak tampil di Detail B-DB
10. Klik breadcrumb "Asset Class"

### TC-FA-FAAC-177: Edit akun tanpa Last Exported Period tersimpan langsung tanpa D-12

11. Baca jumlah versi Asset Class B-ANCHOR sebagai baseline
12. Klik link Class Code "B-ANCHOR" di tabel
13. Klik tab "Accounts" dan ganti Asset Cost menjadi "11002 – Machinery Cost Alt"
14. Klik "Save"
15. Verifikasi muncul toast sukses: "Success, asset class has been updated."
16. Verifikasi tidak muncul dialog "Reclassify Balances"
17. Verifikasi jumlah versi Asset Class B-ANCHOR sama dengan baseline langkah 11 (perubahan Accounts berlaku langsung tanpa membentuk versi)

### TC-FA-FAAC-178: Asset Class Inactive tetap dapat dibuka dan disimpan

18. Klik link Class Code "B-INACT" di tabel
19. Verifikasi halaman Detail terbuka tanpa dialog blok
20. Verifikasi Badge Status "Inactive"
21. Ubah Class Name menjadi "Inactive Renamed"
22. Klik "Save"
23. Verifikasi muncul toast sukses: "Success, asset class has been updated."
24. Verifikasi Class Name "Inactive Renamed" tampil di tabel pada baris B-INACT
25. Verifikasi baris B-INACT tetap berstatus Inactive

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan: 176, 177, 178 (tiap TC memakai Asset Class sendiri).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): `B-DB`, `B-ANCHOR`, `B-INACT` adalah seed bertanda `B-*` per TC, dipakai apa adanya; pemulihan oleh fixture BE.
- Langkah penghubung (S-03): langkah 10 (kembali ke tabel dari Detail yang tidak dirty); langkah 8 membuka ulang Detail B-DB hanya untuk memeriksa Alert versi Scheduled (Expected TC-176 butir c); langkah 11 (baseline jumlah versi, kemampuan baca BE) untuk klausa "tanpa membentuk versi" TC-177.
- Langkah 19 dan 20 dipakai sebagai anchor Detail termuat untuk asersi tanpa dialog blok (bagian 8b butir 2).
- Temuan untuk QA: TC-177 menyebut "tanpa membentuk versi" tanpa cara observasi di UI; spec memakai kemampuan baca BE (disediakan tim FE/BE). TC-178 Post Condition (Class Name berubah) tidak diasersi di luar Expected.

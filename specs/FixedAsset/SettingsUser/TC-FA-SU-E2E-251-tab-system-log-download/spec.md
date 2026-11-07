---
id: TC-FA-SU-E2E-251-tab-system-log-download
title: "Tab System Log: Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-760
coverage:
  web: automated
---

# Tab System Log: Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan System Log (#28). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab System Log Budi Santoso (Pre-setup #28, 7 baris; urutan default Date descending; kolom Name berisi target perubahan). Alias baris yang dipakai langkah (Action | Name | Field):
  - S-1: `Resend Activation Email` | `Hana Kusuma` | `Activation Email`
  - S-2: `Auto-Revert` | `Oscar Pranata` | `Group Manager — IT Infrastructure`
  - S-3: `Edit` | `Oscar Pranata` | `Manage group — IT Infrastructure — Update`
  - S-4: `Assign` | `Lina Marlina` | `Access Level`
  - S-5: `Assign` | `Eka Wulandari` | `Manage group — Finance & Accounting`
  - S-6: `Assign` | `Eka Wulandari` | `Manage accounting`
  - S-7: `Activate` | `Eka Wulandari` | `Status`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed System Log #28 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface System Log dan tidak menambah entri pada Budi Santoso.
- Kemampuan teknis (disediakan tim FE): menangkap berkas hasil unduhan di browser dan membaca isinya (encoding, BOM, nilai sel, nama sheet, urutan baris, dan kolom).

## Test Steps

### TC-FA-SU-760: Cakupan baris dan kolom Download: Search, Filter, Sort, dan Column Visibility

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail pengguna Budi Santoso lalu klik tab System Log
3. Klik icon Download, pilih `Download as CSV`
4. Verifikasi berkas memuat seluruh baris (bukan hanya halaman aktif)
5. Verifikasi urutan baris pada berkas mengikuti sort aktif
6. Ketik Search `Assign`, tekan Enter
7. Klik icon Filter
8. Buka dropdown Name, centang `Eka Wulandari`
9. Klik `[Apply]`
10. Klik icon Download, pilih `Download as CSV`
11. Verifikasi berkas hanya memuat baris yang cocok dengan Search dan Filter (irisan Search `Assign` dan Filter Name `Eka Wulandari`: S-5, S-6 (2 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil))
12. Klik `[Clear Field]` lalu `[Apply]`, lalu klik `(←)` pada kotak Search
13. Klik header Column Visibility (⋯), hilangkan centang Old Value
14. Klik icon Download, pilih `Download as CSV`
15. Verifikasi tidak ada toast peringatan
16. Verifikasi kolom Old Value tidak ikut berkas
17. Klik header Column Visibility (⋯), centang kembali Old Value
18. Klik icon Download, pilih `Download as CSV`
19. Verifikasi kolom Old Value ikut kembali pada berkas
20. Ketik Search `zzzz` (tidak ada hasil), tekan Enter
21. Klik icon Download, pilih `Download as CSV`
22. Verifikasi tidak ada toast
23. Verifikasi berkas terunduh
24. Verifikasi berkas hanya memuat baris header kolom yang visible
25. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (Ketik Search `Budi Santoso` di User List untuk menemukan baris target sebelum membuka Detail, R-16, butir 8b.13); User List memuat 25 pengguna pada 3 halaman sehingga posisi baris tidak diandalkan.
- TC-FA-SU-759 ada di spec 250, TC-FA-SU-761 di spec 373, dan TC-FA-SU-762 di spec 368.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #28 yang disediakan ulang di hook `before` dan `after` (S-14). Aksi spec lain terhadap Budi Santoso menambah entri System Log, sehingga penyediaan ulang seed menjadi syarat asersi urutan dan jumlah baris. (2) TC-FA-SU-760 langkah 3 tidak menyebut kata kunci Search dan opsi Filter; spec memakai Search `Assign` dan Filter Name `Eka Wulandari` (irisan S-5, S-6) serta `zzzz` untuk hasil 0 baris sebagai pilihan sendiri. Hide kolom memakai Old Value.

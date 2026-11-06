---
id: TC-FA-RP-E2E-347-assign-gm-menggantikan-peran-tangga-lain-dengan-asset-admin
title: "Assign Group Manager menggantikan peran tangga lain pada Jenis Transaksi dan node yang sama dengan Asset Admin"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1182
coverage:
  web: automated
---

# Assign Group Manager menggantikan peran tangga lain pada Jenis Transaksi dan node yang sama dengan Asset Admin

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json`; berkas fixture belum ada dan disediakan tim FE): #15 (Ahmad Fauzi, pengguna Standard; target Assign Group Manager), #18 (pohon Group: `IT Infrastructure` > `Data Center`), #19 (seed Role Transaksi; `Data Center` tanpa penugasan manual).
- Precondition TC (dipakai sebagai precondition TC, tidak diasersi): Ahmad Fauzi memegang Staff pada `Data Center` sub-tab `Disposal`. Kondisi itu dibuat lewat seeding API di hook `before` (kemampuan disediakan tim FE/BE, tanpa endpoint karangan).
- Kemampuan teknis: membaca jumlah entri berdasarkan kombinasi kolom pada Changelog Transaction Role sub-tab `Disposal` lewat kemampuan baca yang disediakan tim FE/BE (langkah 1). Entri yang diasersi adalah selisih jumlah terhadap baseline, bukan posisi baris dan bukan total absolut (S-12).
- State yang diubah dan pemulihannya: Assign Group Manager menggantikan baris Staff Ahmad Fauzi di `Data Center` sub-tab `Disposal` dengan baris Asset Admin dan Approver (baris pola), serta menulis penugasan Group Manager di `Data Center`. Changelog bertambah entri (audit trail permanen, tidak dipulihkan). Hook `after` memulihkan Ahmad Fauzi ke state Pre-setup #15 lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state Pre-setup #15 oleh automation baseline"), tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Data Dinamis: tidak ada data yang dibuat spec.
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1182: Assign Group Manager menggantikan peran tangga lain pada Jenis Transaksi dan node yang sama dengan Asset Admin

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Changelog Transaction Role sub-tab `Disposal` untuk kombinasi Action `Remove` Field `Staff — Data Center` Old Value `Ahmad Fauzi`, Action `Assign` Field `Asset Admin — Data Center` New Value `Ahmad Fauzi`, dan Action `Assign (via Group Manager)` Field `Approver — Data Center` New Value `Ahmad Fauzi`
2. Klik Tab `Group Manager`
3. Klik `[+ Assign]` di Tab Group Manager
4. Pilih group `Data Center` pada field Group
5. Ketik Search `Ahmad Fauzi`, tekan Enter pada popup Assign
6. Centang Ahmad Fauzi
7. Klik `[Assign]`
8. Verifikasi tidak muncul dialog konfirmasi apa pun (tidak `D-13`)
9. Verifikasi muncul toast sukses: `Success, Group Manager has been assigned.`
10. Klik Tab `Transaction Role`
11. Klik node `Data Center` di Sidebar Group Tree
12. Klik sub-tab `Disposal`
13. Verifikasi Ahmad Fauzi tampil di section Asset Admin
14. Verifikasi Ahmad Fauzi tampil di section Approver
15. Verifikasi Ahmad Fauzi tidak lagi tampil di section Staff
16. Klik ikon Changelog pada baris sub-tab `Disposal`
17. Verifikasi Changelog memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline langkah 1): Action `Remove`, Field `Staff — Data Center`, Old Value `Ahmad Fauzi`, New Value `—`, Modified By `Siti R`
18. Verifikasi Changelog memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline langkah 1): Action `Assign`, Field `Asset Admin — Data Center`, Old Value `—`, New Value `Ahmad Fauzi`, Modified By `Siti R`
19. Verifikasi Changelog memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline langkah 1): Action `Assign (via Group Manager)`, Field `Approver — Data Center`, Old Value `—`, New Value `Ahmad Fauzi`, Modified By `Siti R`
20. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 20 langkah.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 (baseline entri Changelog, S-12), 2, 10, 11, 12 (membuka Tab, node, dan sub-tab), 5 (Search kandidat di popup Assign, supaya Ahmad Fauzi pasti tampil pada Table User Picker berpaginasi; R-22), 16 dan 20 (membuka dan menutup modal Changelog). Akun aktor pertama sudah login di hook `before` (S-07).
- Urutan Expected a: `Verifikasi` tidak ada dialog (langkah 8) ditulis segera setelah pemicu `[Assign]` dan sebelum toast (8b butir 11); toast langkah 9 menjadi bukti bahwa respons Assign selesai tanpa dialog. Urutan Expected b: tampil di Asset Admin dan Approver (langkah 13 dan 14) ditulis lebih dulu sebagai anchor positif bagi asersi tidak tampil di Staff (langkah 15; 8b butir 2).
- Search tidak dipakai untuk menemukan baris Ahmad Fauzi pada Tab Transaction Role: section `Data Center` sub-tab `Disposal` memuat baris pola dan baris Pre-setup #19 yang sedikit, tidak melebihi satu halaman.
- Pembagian TC lintas spec: TC-FA-RP-1185 (Assign Group Manager bersarang) ada di spec 362; TC-FA-RP-1180 (baris pola Role Transaksi pada Assign Group Manager) ada di spec 361.
- Post Condition TC-FA-RP-1182 ("Ahmad Fauzi dipulihkan ke state Pre-setup #15 oleh automation baseline") tidak punya langkah observasi; tidak diasersi, dipulihkan di hook `after`.
- Temuan untuk QA:
  - Nama Action `Assign (via Group Manager)` (langkah 19) menunggu konfirmasi PM (PRD 12 Open Item #7); spec menulisnya persis seperti TC.
  - Expected c menulis Action `Assign` untuk baris Asset Admin yang menggantikan Staff dan `Assign (via Group Manager)` untuk Approver; TC tidak menetapkan apakah Action baris Asset Admin yang diganti berbeda dari nama itu. Spec menulis Action persis seperti TC dan tidak menambah asersi urutan atau Action lain.
  - Expected c menulis Modified By `Siti R` di akhir kalimat untuk ketiga entri; spec mengasersi Modified By pada masing-masing entri.
  - Precondition d menyatakan Ahmad Fauzi memegang Staff di `Data Center` sub-tab `Disposal`, sedangkan Pre-setup #19 menyatakan `Data Center` tanpa penugasan manual dan Pre-setup #40 mencantumkan Ahmad Fauzi sebagai Asset Admin manual di `IT Infrastructure`. Spec men-seed Precondition d lewat seeding API.
  - Expected a "tanpa dialog konfirmasi apa pun" tidak punya anchor di TC; spec memakai toast sukses sesudah `Verifikasi` tidak ada dialog.
  - Post Condition "dipulihkan ke state Pre-setup #15" tidak punya langkah observasi di TC; tidak diasersi.
  - Asumsi: perilaku Group Manager yang menggantikan peran tangga lain mengikuti TC apa adanya; PRD 12 Open Item #7 belum menetapkan nama Action untuk baris yang diganti.

---
id: TC-FA-LBL-E2E-082-sort-modal-changelog-bagian-2-2
title: "Sort Modal Changelog (bagian 2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-310
  - TC-FA-LBL-311
  - TC-FA-LBL-325
coverage:
  web: automated
---

# Sort Modal Changelog (bagian 2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup #17; pengguna Sarah Johnson), email dari `Fixture.assetLabeling.akun.totalControlChangelog` (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_CHANGELOG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`). Email lengkap Company Changelog tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (`before`, `beforeEach`, `after` pada `suite.md`) berlaku, termasuk flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan state global. Fixture `fixtures/asset-labeling.json` (identitas akun dan nilai seed, tanpa rahasia) belum ada dan disediakan tim FE. Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlChangelog` (belum ada; disediakan tim FE, S-12).
- Data Pre-setup #17 (Company Changelog, hanya dibaca): log Changelog Labels memuat tujuh baris seed (Date 08 sampai 15 Sep 2026): Create `High Priority` (15 Sep 2026 14:20, Sarah J), Edit `High Priority` Color `#DC2626` ke `#EF4444` (15 Sep 2026 14:25, Sarah J), Create `Finance Department` (14 Sep 2026 11:15, David K), Edit `Finance Department` Label Name `Finance Dept` ke `Finance Department` (14 Sep 2026 11:30, David K), Create `Audit Ready` (12 Sep 2026 09:40, Sarah J), Create `Executive Asset` (10 Sep 2026 16:30, Michael W), Delete `Old Tag` (08 Sep 2026 13:00, David K). Entri TC lain (mis. Delete bertanggal hari run dari TC-FA-LBL-325) menambah entri permanen bertanggal hari run sehingga ketujuh baris seed dapat bergeser ke luar halaman pertama (pagination default 10 per halaman). Karena itu spec menerapkan Filter Date `08 Sep 2026` sampai `15 Sep 2026` (rentang inklusif) di Filter Panel Modal Changelog sebelum mengamati baris seed, dan asersi dinilai atas hasil filter itu: tepat tujuh baris seed (entri TC lain berada di luar rentang) (S-12, S-14).
- Data Dinamis (TC-FA-LBL-325): dua label bersih `Tie A 325 {runId}-082` dan `Tie B 325 {runId}-082` (Total Asset 0, bukan Default Label). Dibuat lewat sesi API aktor pada langkah TC-FA-LBL-325 (setelah sort TC-FA-LBL-310 dan TC-FA-LBL-311 selesai) supaya log Create dan Delete-nya tidak memengaruhi tujuh baris seed saat sort. Kedua label dihapus oleh TC itu sendiri; bila spec gagal sebelum Bulk Delete selesai, hook `after` spec ini menghapusnya (lihat Cleanup).
- State global yang diubah: tidak ada. Efek tidak dipulihkan: Changelog Company Changelog (audit trail permanen) bertambah entri Delete (dan entri Create bila seeding mencatat log) untuk kedua label; spec lain yang membaca Company Changelog memakai Filter Date rentang seed atau baseline N dalam rentang itu (Pre-setup #17), bukan total absolut.
- Kemampuan teknis: sesi API aktor (login API password) untuk membuat dua label; seleksi dua baris dan Bulk Delete lewat UI; fixture BE untuk menghapus label `Tie A 325 {runId}-082` dan `Tie B 325 {runId}-082` di hook `after`.
- Cleanup: hook `after` spec ini menghapus label `Tie A 325 {runId}-082` dan `Tie B 325 {runId}-082` lewat fixture BE bila masih ada (tanpa mengasumsikan seeding atau Bulk Delete berhasil; label yang sudah terhapus dilewati), lalu mengembalikan sesi ke akun default suite.

## Test Steps

### Membuka Modal Changelog

1. Klik icon Changelog di Table Tools
2. Klik icon Filter di toolbar modal
3. Pilih rentang `08 Sep 2026` sampai `15 Sep 2026` lalu klik `[Apply]`

### TC-FA-LBL-310: Sort Changelog kolom New Value

4. Klik header kolom `New Value` satu kali
5. Verifikasi atas tujuh baris seed hasil Filter Date klik 1 (Ascending): `#EF4444`, `Audit Ready`, `Executive Asset`, `Finance Department` (Edit lalu Create), `High Priority`, lalu `—` (Delete) di akhir
6. Klik header kolom `New Value` untuk kedua kali
7. Verifikasi atas tujuh baris seed hasil Filter Date klik 2 (Descending): `—` di awal lalu urutan terbalik penuh dari `High Priority` sampai `#EF4444`
8. Klik header kolom `New Value` untuk ketiga kali
9. Verifikasi atas tujuh baris seed hasil Filter Date klik 3 (Netral): kembali ke default Date Newest First

### TC-FA-LBL-311: Sort Changelog kolom Modified By

10. Klik header kolom `Modified By` satu kali
11. Verifikasi atas tujuh baris seed hasil Filter Date klik 1 (Ascending): `David K` (tiga baris), `Michael W` (satu baris), `Sarah J` (tiga baris); dalam kelompok urut Date Newest
12. Klik header kolom `Modified By` untuk kedua kali
13. Verifikasi atas tujuh baris seed hasil Filter Date klik 2 (Descending): `Sarah J`, `Michael W`, lalu `David K`
14. Klik header kolom `Modified By` untuk ketiga kali
15. Verifikasi atas tujuh baris seed hasil Filter Date klik 3 (Netral): kembali ke default Date Newest First

### TC-FA-LBL-325: Entri log dengan Date sama: entri yang ditulis lebih akhir tampil lebih atas

16. Tutup Modal Changelog dengan `[✕]`
17. Buat label `Tie A 325 {runId}-082` lalu `Tie B 325 {runId}-082` lewat sesi API aktor hingga tersimpan
18. Ketik Search `325 {runId}-082`, tekan Enter
19. Centang baris `Tie A 325 {runId}-082` lalu baris `Tie B 325 {runId}-082` (seleksi A kemudian B)
20. Klik `Bulk Action` lalu klik `Delete`
21. Klik `[Delete]` pada dialog `Delete Labels`
22. Tunggu aksi selesai
23. Klik icon Changelog di Table Tools
24. Verifikasi dua entri Delete `Tie A 325 {runId}-082` dan `Tie B 325 {runId}-082` tampil berurutan dengan Date (ketelitian menit) yang sama
25. Verifikasi pada default Newest First entri `Tie B 325 {runId}-082` tampil di atas entri `Tie A 325 {runId}-082`
26. Tutup Modal Changelog dengan `[✕]`
27. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` (bagian 4b).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Klik ketiga pada tiap kolom mengembalikan tabel ke default Date Newest First sehingga TC berikutnya dimulai dari state bersih (S-09).
- Urutan TC: TC-FA-LBL-325 ditaruh paling akhir karena Bulk Delete dan seeding menambah entri log ke Company Changelog; sort TC-FA-LBL-310 dan TC-FA-LBL-311 dinilai atas tujuh baris seed hasil Filter Date `08 Sep 2026` sampai `15 Sep 2026` (langkah 2 dan 3, tetap berlaku untuk kedua TC) sehingga entri bertanggal hari run berada di luar rentang.
- Langkah penghubung (tanpa awalan `Verifikasi`): menutup Modal Changelog, seeding dua label lewat API, Search `325 {runId}-082` untuk menemukan baris target (R-16), `Tunggu aksi selesai` (bagian 8b butir 8; sesudah `[Delete]` langkah berpindah surface ke Modal Changelog), dan `(←)` pada kotak Search di akhir. Seleksi baris tidak perlu dibersihkan karena Bulk Delete menghapus kedua baris.
- Pasangan TC sort bagian 1 (TC-FA-LBL-305 sampai TC-FA-LBL-309) ada di spec 081; TC-FA-LBL-519 ada di spec 168. Detail dialog dan toast Bulk Delete dimiliki TC Bulk Delete di spec lain; spec ini hanya memakai `Bulk Action`, `Delete`, dan `[Delete]`.
- Temuan untuk QA:
  - TC-FA-LBL-325 tidak menyebut apakah seeding label bersih menulis log Create; spec tidak mengasersi entri Create.
  - Email akun Total Control Company Changelog tidak tertulis lengkap di Pre-setup #17 (hanya pola dengan `{namaCompany}`); akun disediakan tim FE.

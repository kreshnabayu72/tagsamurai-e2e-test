---
id: TC-FA-GRP-E2E-078-delete-race-node-dihapus-user-lain-double-click-dan-aksesibilitas-dialog
title: "Delete: Node Dihapus User Lain Sebelum [Delete], Double-Click [Delete], dan Aksesibilitas Dialog (Focus Trap, Esc)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-242
  - TC-FA-GRP-244
  - TC-FA-GRP-245
coverage:
  web: automated
---

# Delete: Node Dihapus User Lain Sebelum [Delete], Double-Click [Delete], dan Aksesibilitas Dialog (Focus Trap, Esc)

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control (Pre-setup No 1: `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`, kosong tanpa aset dan tanpa user ter-scope): `Stale Del` (TC-242), `Del Double` (TC-244), `Del Empty` (TC-245). Data Pre-setup `Warehouse A` (24 aset aktif; Tabel A No 9) hanya dibaca (dialog blokir pada TC-245).
- Pelaku kedua TC-242 ("user lain") menghapus `Stale Del` lewat sesi API (suite.md), bukan konteks UI kedua.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Modal Changelog: Group sebelum dan sesudah aksi (audit trail permanen, tidak dapat diturunkan dari seeding; 8b butir 10) lewat fixture BE atau pembacaan UI.
- Baseline log: N0 = jumlah entri Modal Changelog: Group yang dicatat pada langkah 3, sebelum aksi pemicu pertama yang diasersi (S-12).
- Cleanup di `after`: hapus sisa data milik spec lewat API.

## Test Steps

### Baseline Changelog

1. Buka Modal Changelog: Group
2. Verifikasi sedikitnya satu entri tampil di Modal Changelog: Group
3. Catat jumlah entri Modal Changelog: Group sebagai baseline N0 (jumlah total pada footer pagination)
4. Tutup Modal Changelog: Group

### TC-FA-GRP-242: Node dihapus user lain sebelum [Delete]

5. Buka elipsis `⋯` baris `Stale Del`, pilih `Delete` (dialog terbuka)
6. User lain (sesi API) menghapus `Stale Del` hingga penghapusan tersimpan
7. Klik [Delete] pada dialog
8. Verifikasi dialog tertutup
9. Verifikasi toast netral "This group is no longer available."
10. Verifikasi `Stale Del` tidak lagi ada di tabel dan sidebar (tree di-refresh)
11. Buka Modal Changelog: Group
12. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N0
13. Tutup Modal Changelog: Group

### TC-FA-GRP-244: Double-click [Delete] hanya satu request

14. Buka elipsis `⋯` baris `Del Double`, pilih `Delete`
15. Tunggu toast lama hilang otomatis
16. Klik dua kali cepat [Delete]
17. Verifikasi hanya satu toast yang tampil
18. Verifikasi toast sukses "Success, group has been deleted."
19. Verifikasi `Del Double` hilang dari tabel
20. Buka Modal Changelog: Group
21. Verifikasi jumlah entri Modal Changelog: Group bertambah tepat 1 dibanding baseline N0 (satu entri Delete, tidak ada log ganda)
22. Tutup Modal Changelog: Group

### TC-FA-GRP-245: Aksesibilitas dialog Delete

23. Buka elipsis `⋯` baris `Del Empty`, pilih `Delete`
24. Tekan Tab berulang
25. Verifikasi fokus terkunci di dalam dialog
26. Tekan Esc
27. Verifikasi dialog tertutup (Esc sama dengan [Cancel])
28. Verifikasi `Del Empty` tetap ada di tabel
29. Buka elipsis `⋯` baris `Warehouse A`, pilih `Delete` (dialog blokir)
30. Tekan Esc
31. Verifikasi dialog blokir tertutup (Esc sama dengan [OK])

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 3 dan 4, 6, 11, 13, 15, 20, 22: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Urutan: TC-242 (tidak mengubah log) lebih dulu, lalu TC-244 yang menambah tepat satu entri Delete, lalu TC-245 yang hanya membuka dan menutup dialog (S-10).
- Klausa "tidak ada baris Changelog/System Log/Activity Log baru" TC-242 diasersi pada langkah 12 dengan baseline jumlah entri Modal Changelog: Group; anchor positif: langkah 9 (toast hasil server). Asersi tanpa baris System Log dan Activity Log tidak ditulis: TC tidak memberi cara membaca keduanya (lihat Temuan untuk QA). Langkah 17 (satu toast) didahului hanya satu aksi [Delete] sehingga tidak membutuhkan jeda toast lama (R-12).
- Langkah 28 adalah asersi tambahan (Esc sama dengan [Cancel]: node tidak terhapus) dengan alasan membedakan Cancel dari Delete; tidak ada di Expected TC-245 (S-03).
- Temuan untuk QA:
  - TC-242 Expected b menyebut baris Changelog, System Log, dan Activity Log tanpa menyebut cara membaca System Log dan Activity Log; spec hanya mengasersi Modal Changelog: Group.
  - TC-244 Expected "tidak ada log ganda" tidak menyebut surface; spec memakai Modal Changelog: Group (selisih tepat 1 entri).
  - TC-245 Expected c menyebut dialog plan gating D-06 sampai D-09 tidak menutup lewat Esc, tetapi Precondition dan Langkah tidak memicu dialog tersebut; klausa itu tidak diasersi di spec ini.

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
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Modal Changelog: Group sebelum dan sesudah aksi (audit trail permanen, tidak dapat diturunkan dari seeding; 8b butir 10) lewat fixture BE atau pembacaan UI. Jumlah entri System Log dan Activity Log juga dibaca lewat fixture BE (selisih terhadap baseline, S-12).
- Baseline log: dicatat ulang per TC sesudah pelaku kedua selesai dan tepat sebelum aksi pemicu yang diasersi (S-12): N1 (Modal Changelog: Group, System Log, Activity Log) pada langkah 4 sebelum [Delete] TC-FA-GRP-242, dan N2 (Modal Changelog: Group) pada langkah 16 sebelum klik dua kali [Delete] TC-FA-GRP-244.
- Cleanup di `after`: hapus sisa data milik spec lewat API.

## Test Steps


### TC-FA-GRP-242: Node dihapus user lain sebelum [Delete]

1. Ketik Search `Stale Del`, tekan Enter
2. Buka elipsis `⋯` baris `Stale Del`, pilih `Delete` (dialog terbuka)
3. User lain (sesi API) menghapus `Stale Del` hingga penghapusan tersimpan
4. Catat jumlah entri Modal Changelog: Group, System Log, dan Activity Log sebagai baseline N1 (dibaca lewat fixture BE karena dialog Delete sedang terbuka)
5. Klik [Delete] pada dialog
6. Verifikasi dialog tertutup
7. Verifikasi toast netral "This group is no longer available."
8. Verifikasi `Stale Del` tidak lagi ada di tabel dan sidebar (tree di-refresh)
9. Buka Modal Changelog: Group
10. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N1
11. Verifikasi tidak ada baris baru di System Log dan Activity Log: jumlah entri sama dengan baseline N1 (dibaca lewat fixture BE)
12. Tutup Modal Changelog: Group

### TC-FA-GRP-244: Double-click [Delete] hanya satu request

13. Ganti isi kotak Search dengan `Del Double`, tekan Enter
14. Buka elipsis `⋯` baris `Del Double`, pilih `Delete`
15. Tunggu toast lama hilang otomatis
16. Catat jumlah entri Modal Changelog: Group sebagai baseline N2 (dibaca lewat fixture BE karena dialog Delete sedang terbuka)
17. Klik dua kali cepat [Delete]
18. Verifikasi hanya satu toast yang tampil
19. Verifikasi toast sukses "Success, group has been deleted."
20. Verifikasi `Del Double` hilang dari tabel
21. Buka Modal Changelog: Group
22. Verifikasi jumlah entri Modal Changelog: Group bertambah tepat 1 dibanding baseline N2 (satu entri Delete, tidak ada log ganda)
23. Tutup Modal Changelog: Group

### TC-FA-GRP-245: Aksesibilitas dialog Delete

24. Ganti isi kotak Search dengan `Del Empty`, tekan Enter
25. Buka elipsis `⋯` baris `Del Empty`, pilih `Delete`
26. Tekan Tab berulang
27. Verifikasi fokus terkunci di dalam dialog
28. Tekan Esc
29. Verifikasi dialog tertutup (Esc sama dengan [Cancel])
30. Verifikasi `Del Empty` tetap ada di tabel
31. Ganti isi kotak Search dengan `Warehouse A`, tekan Enter
32. Buka elipsis `⋯` baris `Warehouse A`, pilih `Delete` (dialog blokir)
33. Tekan Esc
34. Verifikasi dialog blokir tertutup (Esc sama dengan [OK])

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 3, 4, 9, 12, 15, 16, 21, 23: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Pencarian baris target (S-03, R-16): langkah 1, 13, 24, 31 (Ketik atau ganti isi kotak Search dengan `Stale Del`, `Del Double`, `Del Empty`, dan `Warehouse A`, tekan Enter) menemukan baris yang dibuka elipsisnya; client memiliki lebih dari 10 node level 1 dan page size 10, jadi baris target tidak dijamin berada di halaman 1 All Groups.
- Urutan: TC-242 (tidak mengubah log) lebih dulu, lalu TC-244 yang menambah tepat satu entri Delete, lalu TC-245 yang hanya membuka dan menutup dialog (S-10).
- Klausa "tidak ada baris Changelog/System Log/Activity Log baru" TC-242 diasersi pada langkah 10 dengan baseline jumlah entri Modal Changelog: Group; anchor positif: langkah 7 (toast hasil server). Klausa tanpa baris System Log dan Activity Log diasersi pada langkah 11 dengan baseline N1 yang dicatat sesudah pelaku kedua selesai (langkah 4), karena penghapusan oleh pelaku kedua sudah menambah entri log (S-12, S-15). Langkah 18 (satu toast) didahului hanya satu aksi [Delete] sehingga tidak membutuhkan jeda toast lama (R-12).
- Langkah 30 adalah asersi tambahan (Esc sama dengan [Cancel]: node tidak terhapus) dengan alasan membedakan Cancel dari Delete; tidak ada di Expected TC-245 (S-03).
- Temuan untuk QA:
  - TC-242 Expected b menyebut baris Changelog, System Log, dan Activity Log tanpa menyebut cara membaca System Log dan Activity Log; spec membaca jumlah entri ketiganya lewat kemampuan baca yang disediakan tim FE/BE (S-15).
  - TC-244 Expected "tidak ada log ganda" tidak menyebut surface; spec memakai Modal Changelog: Group (selisih tepat 1 entri).
  - TC-245 Expected c menyebut dialog plan gating D-06 sampai D-09 tidak menutup lewat Esc, tetapi Precondition dan Langkah tidak memicu dialog tersebut; klausa itu tidak diasersi di spec ini.

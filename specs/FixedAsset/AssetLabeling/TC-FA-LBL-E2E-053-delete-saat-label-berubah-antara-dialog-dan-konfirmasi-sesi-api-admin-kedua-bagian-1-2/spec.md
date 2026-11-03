---
id: TC-FA-LBL-E2E-053-delete-saat-label-berubah-antara-dialog-dan-konfirmasi-sesi-api-admin-kedua-bagian-1-2
title: "Delete Saat Label Berubah Antara Dialog dan Konfirmasi (Sesi API Admin Kedua) (bagian 1/2)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-173
  - TC-FA-LBL-174
  - TC-FA-LBL-197
coverage:
  web: automated
---

# Delete Saat Label Berubah Antara Dialog dan Konfirmasi (Sesi API Admin Kedua) (bagian 1/2)

## Prerequisites

- Mode: FE+BE. Backend nyata pada Company Alpha; tidak ada respons yang di-mock atau di-intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.assetLabeling.totalControl.email`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. `fixtures/asset-labeling.json` belum ada dan disediakan tim FE.
- Hook suite `before`, `beforeEach`, dan `after` (lihat `suite.md`) berlaku. Seeding label di hook `before` spec ini lewat fixture BE; cleanup di hook `after` menghapus label sisa milik spec dan tidak mengasumsikan setup berhasil penuh.
- Data Pre-setup: katalog Company Alpha 9 label (#12); aset `Laptop Dell - 1` (Available, #13) sebagai target lampiran label lewat sesi API; Asset Name `Warehouse Item` (tanpa aset, #14) sebagai target Default Label lewat sesi API. Perubahan pada `Laptop Dell - 1` dan `Warehouse Item` dilepas kembali di `after`; efeknya: Last Updated aset dan Asset Name tersebut berubah (S-06).
- Data Dinamis (label bersih = Total Asset 0, bukan Default Label; nama dasar dari `Fixture.assetLabeling.labels.<kunci>`, suffix `{runId}-053`):
  - TC-FA-LBL-173: `Delete Target 173 {runId}-053` (`deleteTarget173`)
  - TC-FA-LBL-174: `Delete Target 174 {runId}-053` (`deleteTarget174`)
  - TC-FA-LBL-197: `Bulk Clean A 197 {runId}-053` (`bulkCleanA197`)
  - TC-FA-LBL-197: `Bulk Clean B 197 {runId}-053` (`bulkCleanB197`)
- Katalog Company Alpha berisi 9 label Pre-setup #12 ditambah label seed spec ini; spec lain membersihkan datanya sendiri sehingga total di bawah 25 baris dan page size 25 cukup menampilkan seluruhnya tanpa Search.
- Kemampuan teknis: Sesi API aktor: login API password untuk akun Total Control yang sama dengan sesi UI (token tidak dihitung sebagai sesi web), dinyatakan di `suite.md`. Pelaku kedua yang hanya memicu perubahan state (lampiran label ke aset sisi `asset/`, penetapan Default Label sisi `settings-asset-name/`) memakai sesi API itu dan bukan konteks UI kedua. Mekanisme tulis untuk kedua sisi tidak didefinisikan di TC, PRD, atau LLD sehingga disediakan tim FE/BE. Kemampuan baca jumlah entri log per surface (Changelog: Labels, System Log aktor, dan Activity Log) untuk label bernama tertentu: disediakan tim FE/BE (mekanisme tidak didefinisikan di TC, PRD, atau LLD sehingga tidak ada endpoint yang ditulis).
- State global: tidak ada yang diubah. Cleanup di `after`: lepas relasi label seed dari `Laptop Dell - 1`, lepas `Delete Target 174` dari Default Label `Warehouse Item`, lalu hapus label seed.
- Suite berjalan serial (`parallel: false`); spec ini menghapus data sehingga dijalankan sesudah spec non-destruktif.

## Test Steps

1. Atur page size 25

### TC-FA-LBL-173: Label menjadi dipakai antara pembukaan D-01 dan konfirmasi: Delete ditolak dan D-02 menampilkan hitungan terbaru

2. Klik `⋯` pada baris `Delete Target 173 {runId}-053` lalu klik `Delete`
3. Lampirkan label `Delete Target 173 {runId}-053` ke aset `Laptop Dell - 1` lewat sesi API (sisi asset/) hingga tersimpan
4. Catat jumlah entri log label `Delete Target 173 {runId}-053` pada Changelog: Labels, System Log aktor, dan Activity Log (baseline)
5. Klik `[Delete]` pada dialog D-01
6. Verifikasi dialog D-01 digantikan dialog `Cannot Delete Label`
7. Verifikasi dialog memuat baris `This label is assigned to 1 asset.`
8. Verifikasi tidak ada toast tambahan
9. Verifikasi jumlah entri log label `Delete Target 173 {runId}-053` pada Changelog: Labels, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri baru)
10. Klik `[OK]`
11. Verifikasi baris `Delete Target 173 {runId}-053` tetap ada dengan Total Asset `1` (tanpa mutasi)

### TC-FA-LBL-174: Label menjadi Default Label antara pembukaan D-01 dan konfirmasi: D-02 menampilkan Default Label

12. Klik `⋯` pada baris `Delete Target 174 {runId}-053` lalu klik `Delete`
13. Jadikan `Delete Target 174 {runId}-053` Default Label Asset Name `Warehouse Item` lewat sesi API (sisi settings-asset-name/) hingga tersimpan
14. Catat jumlah entri log label `Delete Target 174 {runId}-053` pada Changelog: Labels, System Log aktor, dan Activity Log (baseline)
15. Klik `[Delete]` pada dialog D-01
16. Verifikasi dialog `Cannot Delete Label` tampil
17. Verifikasi dialog memuat baris `This label is used as Default Label by 1 asset name.`
18. Verifikasi dialog tidak memuat baris jumlah aset
19. Verifikasi jumlah entri log label `Delete Target 174 {runId}-053` pada Changelog: Labels, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri baru)
20. Klik `[OK]`
21. Verifikasi baris `Delete Target 174 {runId}-053` tetap ada (tanpa mutasi)

### TC-FA-LBL-197: Semua label bersih menjadi dipakai sebelum konfirmasi: D-05 tampil tanpa penghapusan

22. Centang `Bulk Clean A 197 {runId}-053` dan `Bulk Clean B 197 {runId}-053`
23. Klik `Bulk Action` lalu klik `Delete`
24. Lampirkan `Bulk Clean A 197 {runId}-053` dan `Bulk Clean B 197 {runId}-053` ke aset `Laptop Dell - 1` lewat sesi API hingga tersimpan
25. Catat jumlah entri log label `Bulk Clean A 197 {runId}-053` dan `Bulk Clean B 197 {runId}-053` pada Changelog: Labels, System Log aktor, dan Activity Log (baseline)
26. Klik `[Delete]` pada dialog D-03
27. Verifikasi dialog `Cannot Delete Labels` dengan bullet `• Bulk Clean A 197 {runId}-053` dan `• Bulk Clean B 197 {runId}-053` serta teks `These labels are in use and cannot be deleted.`
28. Verifikasi tidak ada toast partial
29. Verifikasi tidak ada penghapusan: baris `Bulk Clean A 197 {runId}-053` dan `Bulk Clean B 197 {runId}-053` tetap ada
30. Verifikasi jumlah entri log label `Bulk Clean A 197 {runId}-053` dan `Bulk Clean B 197 {runId}-053` pada Changelog: Labels, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri baru)
31. Klik `[OK]`
32. Verifikasi seleksi dan Bulk Action Bar dipertahankan

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 1 (page size 25 supaya seluruh label spec tampil tanpa Search); klik `[OK]` menutup dialog D-02 dan D-05 sebelum Verifikasi keadaan akhir; baris baseline log (dicatat tepat sebelum klik `[Delete]` yang diasersi, S-12). Spec berakhir dengan seleksi TC-FA-LBL-197 dipertahankan karena itu hasil yang diasersi; hook `after` dan pembukaan halaman berikutnya oleh suite membersihkannya.
- P-1 (state berat): asersi "tidak ada entri log" TC-FA-LBL-173, TC-FA-LBL-174, dan TC-FA-LBL-197 ditulis di spec ini dengan baseline jumlah entri (S-12) karena konteksnya bergantung pada dialog yang dibuka lebih dulu lalu state label diubah pihak lain; pemicu itu tidak bisa dipindah ke spec absence tanpa membangun ulang state yang sama.
- Langkah pemicu pelaku kedua lewat sesi API ditulis "... hingga ... tersimpan" dan tidak memakai `P-2` (bagian 3 prinsip 13, 2026-10-30).
- Pembagian TC lintas spec: TC-FA-LBL-196, TC-FA-LBL-198, TC-FA-LBL-199, dan TC-FA-LBL-468 (Delete saat label berubah atau dihapus pihak lain) ada di spec 054.
- Temuan untuk QA:
  - TC-FA-LBL-197 langkah 3 ("Lampirkan keduanya ke aset lewat API") tidak menyebut aset target; spec memakai `Laptop Dell - 1` (Pre-setup #13) seperti TC-FA-LBL-173. Melampirkan dan melepas label pada aset Pre-setup mengubah Last Updated aset itu; spec lain yang mengasersi Last Updated `Laptop Dell - 1` terdampak.
  - Cara menulis relasi label dan Default Label lewat API (sisi asset/ dan settings-asset-name/) tidak didefinisikan di TC, PRD, atau LLD; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE (S-13).
  - Post Condition TC-FA-LBL-173 (label tetap ada dengan Total Asset `1`) tidak punya langkah observasi; Verifikasi baris tetap ada diturunkan dari Expected b ("tidak ada mutasi").
  - Expected tiga TC ini tidak menyebut surface log; spec memakai tiga surface pencatatan (Changelog: Labels, System Log aktor, dan Activity Log) mengikuti Post Condition TC-FA-LBL-160.

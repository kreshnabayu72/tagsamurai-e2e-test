---
id: TC-FA-LBL-E2E-054-delete-saat-label-berubah-antara-dialog-dan-konfirmasi-sesi-api-admin-kedua-bagian-2-2
title: "Delete Saat Label Berubah Antara Dialog dan Konfirmasi (Sesi API Admin Kedua) (bagian 2/2)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-196
  - TC-FA-LBL-198
  - TC-FA-LBL-199
  - TC-FA-LBL-468
coverage:
  web: automated
---

# Delete Saat Label Berubah Antara Dialog dan Konfirmasi (Sesi API Admin Kedua) (bagian 2/2)

## Prerequisites

- Mode: FE+BE. Backend nyata pada Company Alpha; tidak ada respons yang di-mock atau di-intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.assetLabeling.totalControl.email`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. `fixtures/asset-labeling.json` belum ada dan disediakan tim FE.
- Akun pelaku kedua (sesi API saja): Total Control sesi 2 (Pre-setup #9), `totalControlSecond_automated_{namaCompany}@qwertysystem.net` (`Fixture.assetLabeling.totalControlSecond.email`), password `Spectra.env.FA_TC2_PASSWORD`.
- Hook suite `before`, `beforeEach`, dan `after` (lihat `suite.md`) berlaku. Seeding label di hook `before` spec ini lewat fixture BE; cleanup di hook `after` menghapus label sisa milik spec dan tidak mengasumsikan setup berhasil penuh.
- Data Pre-setup: katalog Company Alpha 9 label (#12); aset `Laptop Dell - 1` (Available, #13) sebagai target lampiran `Bulk Clean B 196` lewat sesi API; relasi itu dilepas di `after` dan efeknya: Last Updated aset berubah (S-06).
- Data Dinamis (label bersih = Total Asset 0, bukan Default Label; nama dasar dari `Fixture.assetLabeling.labels.<kunci>`, suffix `{runId}-054`):
  - TC-FA-LBL-196: `Bulk Clean A 196 {runId}-054` (`bulkCleanA196`)
  - TC-FA-LBL-196: `Bulk Clean B 196 {runId}-054` (`bulkCleanB196`)
  - TC-FA-LBL-198: `Bulk Clean A 198 {runId}-054` (`bulkCleanA198`)
  - TC-FA-LBL-198: `Bulk Clean B 198 {runId}-054` (`bulkCleanB198`)
  - TC-FA-LBL-199: `Bulk Clean A 199 {runId}-054` (`bulkCleanA199`)
  - TC-FA-LBL-199: `Bulk Clean B 199 {runId}-054` (`bulkCleanB199`)
  - TC-FA-LBL-468: `Race Del 468 {runId}-054` (`raceDel468`)
- Katalog Company Alpha berisi 9 label Pre-setup #12 ditambah label seed spec ini; spec lain membersihkan datanya sendiri sehingga total di bawah 25 baris dan page size 25 cukup menampilkan seluruhnya tanpa Search.
- Kemampuan teknis: Sesi API aktor: login API password untuk akun Total Control yang sama dengan sesi UI (token tidak dihitung sebagai sesi web), dinyatakan di `suite.md`. Pelaku kedua (menghapus label, melampirkan label ke aset) memakai sesi API itu, untuk TC-FA-LBL-468 dengan akun sesi 2 (`FA_TC2_PASSWORD`); sesi UI kedua tidak dibuka karena hasil di sesi itu tidak diasersi. Mekanisme tulis tidak didefinisikan di TC, PRD, atau LLD sehingga disediakan tim FE/BE. Kemampuan baca jumlah entri log per surface (Changelog: Labels, System Log aktor, dan Activity Log) untuk label bernama tertentu: disediakan tim FE/BE (mekanisme tidak didefinisikan di TC, PRD, atau LLD sehingga tidak ada endpoint yang ditulis).
- State global: tidak ada yang diubah. Cleanup di `after`: lepas relasi `Bulk Clean B 196` dari `Laptop Dell - 1`, lalu hapus label seed yang tersisa.
- Suite berjalan serial (`parallel: false`); spec ini menghapus data sehingga dijalankan sesudah spec non-destruktif.

## Test Steps

1. Atur page size 25

### TC-FA-LBL-196: Label bersih menjadi dipakai sebelum konfirmasi bulk: item dilewati dan dilaporkan sebagai sebagian

2. Centang `Bulk Clean A 196 {runId}-054` dan `Bulk Clean B 196 {runId}-054`
3. Klik `Bulk Action` lalu klik `Delete`
4. Lampirkan `Bulk Clean B 196 {runId}-054` ke aset `Laptop Dell - 1` lewat sesi API hingga tersimpan
5. Klik `[Delete]` pada dialog D-03
6. Verifikasi toast `Success, label has been deleted. Some items were skipped.`
7. Verifikasi `Bulk Clean A 196 {runId}-054` terhapus: baris tidak ada lagi di tabel
8. Verifikasi `Bulk Clean B 196 {runId}-054` tetap ada dengan Total Asset `1`

### TC-FA-LBL-199: Seluruh label terpilih sudah dihapus pengguna lain saat konfirmasi bulk

9. Centang `Bulk Clean A 199 {runId}-054` dan `Bulk Clean B 199 {runId}-054`
10. Klik `Bulk Action` lalu klik `Delete`
11. Hapus `Bulk Clean A 199 {runId}-054` dan `Bulk Clean B 199 {runId}-054` lewat sesi API hingga terhapus
12. Catat jumlah entri log label `Bulk Clean A 199 {runId}-054` dan `Bulk Clean B 199 {runId}-054` pada Changelog: Labels, System Log aktor, dan Activity Log sesudah penghapusan lewat API (baseline)
13. Klik `[Delete]` pada dialog D-03
14. Verifikasi toast `This label is no longer available.`
15. Verifikasi tidak ada toast partial
16. Verifikasi Bulk Action Bar hilang dan seleksi 0
17. Verifikasi tabel di-refresh: baris `Bulk Clean A 199 {runId}-054` dan `Bulk Clean B 199 {runId}-054` tidak ada lagi
18. Verifikasi jumlah entri log label `Bulk Clean A 199 {runId}-054` dan `Bulk Clean B 199 {runId}-054` pada Changelog: Labels, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri baru)

### TC-FA-LBL-198: Sebagian label sudah dihapus pengguna lain saat konfirmasi bulk

19. Centang `Bulk Clean A 198 {runId}-054` dan `Bulk Clean B 198 {runId}-054`
20. Klik `Bulk Action` lalu klik `Delete`
21. Hapus `Bulk Clean B 198 {runId}-054` lewat sesi API hingga terhapus
22. Catat jumlah entri log label `Bulk Clean B 198 {runId}-054` pada Changelog: Labels, System Log aktor, dan Activity Log sesudah penghapusan lewat API (baseline)
23. Klik `[Delete]` pada dialog D-03
24. Verifikasi toast `Success, label has been deleted. Some items were skipped.`
25. Verifikasi `Bulk Clean A 198 {runId}-054` terhapus: baris tidak ada lagi di tabel
26. Verifikasi jumlah entri log label `Bulk Clean B 198 {runId}-054` pada Changelog: Labels, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri baru)

### TC-FA-LBL-468: Delete label yang sudah dihapus admin lain

27. Klik `⋯` pada baris `Race Del 468 {runId}-054` lalu klik `Delete`
28. Hapus `Race Del 468 {runId}-054` lewat sesi API akun Total Control sesi 2 hingga terhapus
29. Catat jumlah entri log label `Race Del 468 {runId}-054` pada Changelog: Labels, System Log aktor, dan Activity Log sesudah penghapusan lewat API (baseline)
30. Klik `[Delete]` pada dialog `Delete Label` di sesi 1
31. Verifikasi sesi 1: toast `This label is no longer available.`
32. Verifikasi sesi 1: dialog tertutup
33. Verifikasi sesi 1: tabel di-refresh, baris `Race Del 468 {runId}-054` tidak ada lagi
34. Verifikasi jumlah entri log label `Race Del 468 {runId}-054` pada Changelog: Labels, System Log aktor, dan Activity Log sama dengan baseline (tidak ada entri baru dari sesi 1)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: TC-FA-LBL-196, TC-FA-LBL-199, TC-FA-LBL-198, TC-FA-LBL-468 (bukan urutan nomor) supaya toast `Success, label has been deleted. Some items were skipped.` dan `This label is no longer available.` tidak muncul berurutan dengan teks yang sama; toast terdahulu bisa masih tampil saat toast berikutnya diasersi (R-12).
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 1 (page size 25 supaya seluruh label spec tampil tanpa Search); baris baseline log (dicatat tepat sebelum klik `[Delete]` yang diasersi, sesudah penghapusan lewat API, S-12).
- P-1 (state berat): asersi "tidak ada entri log" TC-FA-LBL-198, TC-FA-LBL-199, dan TC-FA-LBL-468 ditulis di spec ini dengan baseline jumlah entri (S-12) karena konteksnya bergantung pada dialog yang dibuka lebih dulu lalu state label diubah pihak lain; pemicu itu tidak bisa dipindah ke spec absence tanpa membangun ulang state yang sama.
- Langkah pemicu pelaku kedua lewat sesi API ditulis "... hingga ... tersimpan" atau "... hingga terhapus" dan tidak memakai `P-2` (bagian 3 prinsip 13, 2026-10-30). TC-FA-LBL-468 Langkah 1 menyebut sesi 2 membuka dialog `Delete Label`; spec tidak membukanya di sesi UI kedua karena hasil di sesi 2 tidak diasersi, sesi 2 hanya menghapus label lewat API.
- Pembagian TC lintas spec: TC-FA-LBL-173, TC-FA-LBL-174, dan TC-FA-LBL-197 ada di spec 053.
- Temuan untuk QA:
  - Expected TC-FA-LBL-198 b ("tidak ada entri log untuk `Bulk Clean B 198`") dan TC-FA-LBL-199 b ("tidak ada entri log") ambigu: penghapusan label lewat API oleh pihak lain tentu menulis entri Delete-nya sendiri. Spec menafsirkan sebagai tidak ada entri baru dari aksi bulk di sesi UI relatif terhadap baseline yang dicatat sesudah penghapusan lewat API.
  - Expected TC-FA-LBL-468 b ("Tidak ada entri log baru dari sesi 1") dan Expected pada ketiga TC lain tidak menyebut surface log; spec memakai tiga surface pencatatan (Changelog: Labels, System Log aktor, dan Activity Log) mengikuti Post Condition TC-FA-LBL-160.
  - Post Condition TC-FA-LBL-196 ("Entri Delete hanya untuk `Bulk Clean A 196`") tidak punya langkah observasi di TC dan tidak diasersi.
  - Cara menulis relasi label dan menghapus label lewat API tidak didefinisikan di TC, PRD, atau LLD; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE (S-13).

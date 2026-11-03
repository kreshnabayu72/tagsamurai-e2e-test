---
id: TC-FA-LBL-E2E-055-bulk-delete-dialog-d-03-homogen-bersih-dan-seleksi
title: "Bulk Delete: Dialog D-03 Homogen Bersih dan Seleksi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-185
  - TC-FA-LBL-187
  - TC-FA-LBL-188
  - TC-FA-LBL-189
  - TC-FA-LBL-203
  - TC-FA-LBL-498
coverage:
  web: automated
---

# Bulk Delete: Dialog D-03 Homogen Bersih dan Seleksi

## Prerequisites

- Mode: FE+BE. Backend nyata pada Company Alpha; tidak ada respons yang di-mock atau di-intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. `fixtures/asset-labeling.json` belum ada dan disediakan tim FE.
- Hook suite `before`, `beforeEach`, dan `after` (lihat `suite.md`) berlaku. Seeding label di hook `before` spec ini lewat fixture BE; cleanup di hook `after` menghapus label sisa milik spec dan tidak mengasumsikan setup berhasil penuh.
- Data Pre-setup: katalog Company Alpha 9 label (#12), hanya tampil dan tidak diubah.
- Data Dinamis (label bersih = Total Asset 0, bukan Default Label; nama dasar dari `Fixture.assetLabeling.labels.<kunci>`, suffix `{runId}-055`):
  - TC-FA-LBL-185: `Bulk Clean A 185 {runId}-055` (`bulkCleanA185`)
  - TC-FA-LBL-187: `Bulk Clean A 187 {runId}-055` (`bulkCleanA187`)
  - TC-FA-LBL-187: `Bulk Clean B 187 {runId}-055` (`bulkCleanB187`)
  - TC-FA-LBL-188: `Bulk Clean A 188 {runId}-055` (`bulkCleanA188`)
  - TC-FA-LBL-188: `Bulk Clean B 188 {runId}-055` (`bulkCleanB188`)
  - TC-FA-LBL-189: `Bulk Clean A 189 {runId}-055` (`bulkCleanA189`)
  - TC-FA-LBL-189: `Bulk Clean B 189 {runId}-055` (`bulkCleanB189`)
  - TC-FA-LBL-498: `Bulk Double A 498 {runId}-055` (`bulkDoubleA498`)
  - TC-FA-LBL-498: `Bulk Double B 498 {runId}-055` (`bulkDoubleB498`)
  - TC-FA-LBL-203 memakai label TC-FA-LBL-189 (langkahnya identik, satu eksekusi).
- Katalog Company Alpha berisi 9 label Pre-setup #12 ditambah label seed spec ini; spec lain membersihkan datanya sendiri sehingga total di bawah 25 baris dan page size 25 cukup menampilkan seluruhnya tanpa Search.
- Kemampuan teknis: seeding label lewat fixture BE; klik ganda cepat pada satu tombol; Kemampuan baca jumlah entri log per surface (Changelog: Labels, System Log aktor, dan Activity Log) untuk label bernama tertentu: disediakan tim FE/BE (mekanisme tidak didefinisikan di TC, PRD, atau LLD sehingga tidak ada endpoint yang ditulis).
- State global: tidak ada yang diubah. Label TC-FA-LBL-185, 187, dan 188 tetap ada sampai `after`; label TC-FA-LBL-189 dan 498 dihapus oleh spec.
- Suite berjalan serial (`parallel: false`); spec ini menghapus data sehingga dijalankan sesudah spec non-destruktif.

## Test Steps

1. Atur page size 25

### TC-FA-LBL-185: Bulk dengan 1 baris terpilih bersih memakai dialog single D-01

2. Centang baris `Bulk Clean A 185 {runId}-055`
3. Klik `Bulk Action` lalu klik `Delete`
4. Verifikasi dialog `Delete Label` (singular) dengan bullet `• Bulk Clean A 185 {runId}-055` dan `Are you sure you want to delete it? This action cannot be undone.`
5. Verifikasi dialog bukan dialog `Delete Labels`
6. Klik `[Cancel]`
7. Klik ikon `×`

### TC-FA-LBL-187: Screening dialog Bulk Delete homogen bersih (D-03)

8. Centang `Bulk Clean B 187 {runId}-055` lalu `Bulk Clean A 187 {runId}-055` (urutan klik B lalu A)
9. Klik `Bulk Action` lalu klik `Delete`
10. Verifikasi dialog Title `Delete Labels`
11. Verifikasi body bullet nama terurut abjad A sampai Z: `• Bulk Clean A 187 {runId}-055` lalu `• Bulk Clean B 187 {runId}-055`, diikuti `Are you sure you want to delete them? This action cannot be undone.`
12. Verifikasi tombol `[Cancel]` dan `[Delete]` (danger/merah) tampil
13. Klik `[Cancel]`
14. Klik ikon `×`

### TC-FA-LBL-188: Cancel pada D-03 tidak mereset seleksi

15. Centang `Bulk Clean A 188 {runId}-055` dan `Bulk Clean B 188 {runId}-055`
16. Klik `Bulk Action` lalu klik `Delete`
17. Klik `[Cancel]`
18. Verifikasi dialog tertutup
19. Verifikasi seleksi dan Bulk Action Bar dipertahankan dengan counter `2 Labels selected`
20. Verifikasi tidak ada penghapusan: baris `Bulk Clean A 188 {runId}-055` dan `Bulk Clean B 188 {runId}-055` tetap ada
21. Klik ikon `×`

### TC-FA-LBL-498: Klik ganda cepat pada Delete di dialog Bulk Delete hanya memproses satu request

22. Centang `Bulk Double A 498 {runId}-055` dan `Bulk Double B 498 {runId}-055`
23. Klik `Bulk Action` lalu klik `Delete`
24. Tunggu toast lama hilang, lalu klik `[Delete]` dua kali dengan cepat
25. Verifikasi hanya satu toast `Success, label has been deleted.`
26. Verifikasi tidak ada toast error `This label is no longer available.`
27. Verifikasi satu entri Delete per label tercatat: tepat satu untuk `Bulk Double A 498 {runId}-055` dan tepat satu untuk `Bulk Double B 498 {runId}-055` (dua entri, bukan empat) pada Changelog: Labels, System Log aktor, dan Activity Log (baseline nol karena nama bersuffix unik)

### TC-FA-LBL-189 dan TC-FA-LBL-203: Konfirmasi D-03 menghapus semua label terpilih; bar hilang dan seleksi ter-reset ke 0

28. Centang `Bulk Clean A 189 {runId}-055` dan `Bulk Clean B 189 {runId}-055`
29. Klik `Bulk Action` lalu klik `Delete`
30. Klik `[Delete]`
31. Verifikasi toast `Success, label has been deleted.`
32. Verifikasi kedua baris `Bulk Clean A 189 {runId}-055` dan `Bulk Clean B 189 {runId}-055` hilang dari tabel
33. Verifikasi Bulk Action Bar hilang dengan seleksi 0
34. Verifikasi tabel di-refresh

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: TC-FA-LBL-498 mendahului TC-FA-LBL-189 dan TC-FA-LBL-203 supaya hitungan "hanya satu toast" tidak bertemu toast sukses sebelumnya (R-12) dan karena aksi yang menghapus data berada di akhir (S-10).
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 1 (page size 25 supaya seluruh label spec tampil tanpa Search); klik `[Cancel]` dan klik ikon `×` di akhir TC-FA-LBL-185, TC-FA-LBL-187, dan TC-FA-LBL-188 menutup dialog dan membersihkan seleksi sebelum TC berikutnya (S-09).
- Pembagian TC: TC-FA-LBL-203 dan TC-FA-LBL-189 memiliki langkah identik (centang dua label, `Bulk Action` > `Delete`, `[Delete]`), sehingga satu eksekusi menjawab Expected kedua TC dengan data TC-FA-LBL-189; Verifikasi bar hilang, seleksi 0, dan tabel di-refresh berasal dari TC-FA-LBL-203. Dua label bersih kedua TC-FA-LBL-185 (`Bulk Clean B 185`) tidak di-seed karena tidak dipakai langkah maupun Verifikasi (S-11).
- Pencatatan log: Post Condition TC-FA-LBL-189 b (satu entri Delete per label, tampil berurutan dengan Date ketelitian menit yang sama) tidak punya langkah observasi di TC dan tidak diasersi; asersi log itu ada di TC Section 5. Asersi absence log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - Expected b TC-FA-LBL-498 ("Satu entri Delete per label tercatat") tidak menyebut surface log; spec memakai tiga surface pencatatan (Changelog: Labels, System Log aktor, dan Activity Log) mengikuti Post Condition TC-FA-LBL-160.
  - Post Condition TC-FA-LBL-189 b (entri Delete dengan Date ketelitian menit yang sama) tidak diasersi karena TC tidak memberi langkah observasi.
  - TC-FA-LBL-185 Precondition menyebut dua label bersih tetapi hanya `Bulk Clean A 185` yang dipakai Langkah Uji dan Expected.

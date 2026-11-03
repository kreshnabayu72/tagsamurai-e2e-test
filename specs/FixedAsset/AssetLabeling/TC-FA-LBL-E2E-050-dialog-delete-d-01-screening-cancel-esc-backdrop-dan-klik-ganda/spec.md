---
id: TC-FA-LBL-E2E-050-dialog-delete-d-01-screening-cancel-esc-backdrop-dan-klik-ganda
title: "Dialog Delete D-01: Screening, Cancel, Esc/Backdrop, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-157
  - TC-FA-LBL-158
  - TC-FA-LBL-159
  - TC-FA-LBL-172
coverage:
  web: automated
---

# Dialog Delete D-01: Screening, Cancel, Esc/Backdrop, dan Klik Ganda

## Prerequisites

- Mode: FE+BE. Backend nyata pada Company Alpha; tidak ada respons yang di-mock atau di-intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.assetLabeling.totalControl.email`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. `fixtures/asset-labeling.json` belum ada dan disediakan tim FE.
- Hook suite `before`, `beforeEach`, dan `after` (lihat `suite.md`) berlaku. Seeding label di hook `before` spec ini lewat fixture BE; cleanup di hook `after` menghapus label sisa milik spec dan tidak mengasumsikan setup berhasil penuh.
- Data Pre-setup: katalog Company Alpha 9 label (Pre-setup #12), hanya tampil dan tidak diubah.
- Data Dinamis (label bersih = Total Asset 0, bukan Default Label; nama dasar dari `Fixture.assetLabeling.labels.<kunci>`, suffix `{runId}-050`):
  - TC-FA-LBL-157: `Delete Target 157 {runId}-050` (`deleteTarget157`)
  - TC-FA-LBL-158: `Delete Target 158 {runId}-050` (`deleteTarget158`)
  - TC-FA-LBL-159: `Delete Target 159 {runId}-050` (`deleteTarget159`)
  - TC-FA-LBL-172: `Delete Target 172 {runId}-050` (`deleteTarget172`)
- Katalog Company Alpha berisi 9 label Pre-setup #12 ditambah label seed spec ini; spec lain membersihkan datanya sendiri sehingga total di bawah 25 baris dan page size 25 cukup menampilkan seluruhnya tanpa Search.
- Kemampuan teknis: seeding label lewat fixture BE; klik ganda cepat pada satu tombol; Kemampuan baca jumlah entri log per surface (Changelog: Labels, System Log aktor, dan Activity Log) untuk label bernama tertentu: disediakan tim FE/BE (mekanisme tidak didefinisikan di TC, PRD, atau LLD sehingga tidak ada endpoint yang ditulis).
- State global: tidak ada yang diubah. Label `Delete Target 157`, `158`, dan `159` tetap ada sampai `after`; `Delete Target 172` dihapus oleh spec.
- Suite berjalan serial (`parallel: false`); spec ini menghapus data sehingga dijalankan sesudah spec non-destruktif.

## Test Steps

1. Atur page size 25

### TC-FA-LBL-157: Screening dialog konfirmasi Delete label bersih (D-01)

2. Klik `⋯` pada baris `Delete Target 157 {runId}-050` lalu klik `Delete`
3. Verifikasi title dialog `Delete Label`
4. Verifikasi body dialog: bullet `• Delete Target 157 {runId}-050` diikuti `Are you sure you want to delete it? This action cannot be undone.`
5. Verifikasi tombol `[Cancel]` (Button Text, Contrast) dan tombol `[Delete]` (danger/merah) tampil
6. Klik area gelap di luar dialog
7. Verifikasi dialog tidak menutup saat area di luar dialog diklik
8. Klik `[Cancel]`

### TC-FA-LBL-158: Cancel pada dialog D-01 menutup dialog tanpa menghapus

9. Klik `⋯` pada baris `Delete Target 158 {runId}-050` lalu klik `Delete`
10. Klik `[Cancel]`
11. Verifikasi dialog tertutup
12. Verifikasi tidak ada toast
13. Verifikasi baris `Delete Target 158 {runId}-050` tetap ada di tabel

### TC-FA-LBL-159: Esc dan klik backdrop pada dialog D-01

14. Klik `⋯` pada baris `Delete Target 159 {runId}-050` lalu klik `Delete`
15. Klik area gelap di luar dialog
16. Verifikasi klik backdrop tidak menutup dialog
17. Tekan Esc
18. Verifikasi Esc menutup dialog setara `[Cancel]`
19. Verifikasi label tidak dihapus: baris `Delete Target 159 {runId}-050` tetap ada di tabel

### TC-FA-LBL-172: Klik ganda cepat pada Delete hanya memproses satu request

20. Klik `⋯` pada baris `Delete Target 172 {runId}-050` lalu klik `Delete`
21. Tunggu toast lama hilang, lalu klik `[Delete]` dua kali dengan cepat
22. Verifikasi hanya satu toast sukses `Success, label has been deleted.` tampil
23. Verifikasi tidak ada toast error `This label is no longer available.` dari klik kedua
24. Verifikasi tepat satu entri Delete untuk `Delete Target 172 {runId}-050` tercatat pada Changelog: Labels, System Log aktor, dan Activity Log (baseline nol karena nama bersuffix unik)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 1 (page size 25 supaya seluruh label spec tampil tanpa Search, sehingga baris target tidak dicari lewat Search); langkah 8 (menutup dialog TC-FA-LBL-157 sebelum TC berikutnya, S-09); klik area gelap pada TC-FA-LBL-157 dan TC-FA-LBL-159.
- Pencatatan log: asersi absence log tidak ada di spec ini (S-05). Post Condition TC-FA-LBL-158 ("tidak ada entri log") tidak punya langkah observasi di TC dan tidak diasersi. TC-FA-LBL-172 memakai asersi jumlah (bukan absence) dengan nama bersuffix unik sebagai baseline nol (S-12).
- Temuan untuk QA:
  - TC-FA-LBL-157 Expected d (dialog tidak menutup saat area di luar dialog diklik) tidak punya langkah klik backdrop di Langkah Uji; spec menambahkan klik area gelap sebagai langkah penghubung.
  - Expected TC-FA-LBL-172 ("satu entri Delete tercatat") tidak menyebut surface log; spec memakai tiga surface pencatatan (Changelog: Labels, System Log aktor, dan Activity Log) mengikuti Post Condition TC-FA-LBL-160.
  - Post Condition TC-FA-LBL-158 (Label tidak berubah dan tidak ada entri log) tidak diasersi karena TC tidak memberi langkah observasi log.

---
id: TC-FA-PREF-E2E-098-modal-changelog-urutan-default-date-newest-first-nilai-kosong-tanda-strip-tutup-modal-dan-empty-state
title: "Modal Changelog: Urutan Default Date Newest First, Nilai Kosong Tanda Strip, Tutup Lewat X, Esc, Klik Luar, dan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-27
  - TC-FA-PREF-28
  - TC-FA-PREF-292
  - TC-FA-PREF-293
  - TC-FA-PREF-294
  - TC-FA-PREF-297
coverage:
  web: automated
---

# Modal Changelog: Urutan Default Date Newest First, Nilai Kosong Tanda Strip, Tutup Lewat X, Esc, Klik Luar, dan Empty State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-1 dan PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup (hanya dibaca, tidak diubah): Preferences nilai awal PA-2 untuk TC-FA-PREF-27 dan 28 dan PB-1 untuk TC-FA-PREF-292, 293, 294, dan 297 (setara: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date; tidak terkunci); Changelog Preferences berisi 9 entri contoh PA-17 untuk TC-FA-PREF-27 dan 28 dan PB-C1 untuk TC-FA-PREF-292, 293, dan 294 (setara; Date 27/10/26 16:40 sampai 20/10/26 09:12, Modified By "Budi S" dan "Rina A", format tanggal dd/MM/yy dan 24 jam); Changelog Preferences tanpa entri (PB-C0) untuk TC-FA-PREF-297. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API); seed ulang PB-C0 dan pemulihan PB-C1 dilakukan lewat langkah penghubung (langkah 19 dan 24). Seed PA-17 dan PB-C1 mengatur Changelog company seed ke tepat 9 entri (lihat Temuan untuk QA).
- State yang diubah spec: Changelog Preferences company diatur kosong pada langkah 19 dan dipulihkan ke PB-C1 pada langkah 24 dan di hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-27: Modal Changelog terbuka dengan urutan default Date Newest First

1. Klik ikon View history
2. Verifikasi modal Changelog terbuka
3. Verifikasi baris terurut kolom Date dari terbaru ke terlama: entri 27/10/26 16:40 di baris pertama dan entri Create 20/10/26 09:12 di baris terakhir
4. Verifikasi kolom Date menampilkan indikator sort Newest First

### TC-FA-PREF-28: Nilai kosong pada kolom Old Value dan New Value Changelog tampil sebagai tanda strip

5. Verifikasi Old Value baris Default Capitalization Offset (27/10/26 16:40) tampil "—"
6. Verifikasi Old Value baris Create (20/10/26 09:12) tampil "—"
7. Verifikasi New Value baris Default Gain on Disposal (24/10/26 10:02) tampil "—"

### TC-FA-PREF-292: Tutup modal Changelog lewat ikon [✕]

8. Klik ikon [✕] di header modal
9. Verifikasi modal Changelog tertutup
10. Verifikasi Tab "Preferences" tampil tanpa perubahan

### TC-FA-PREF-293: Tutup modal Changelog lewat tombol Esc

11. Klik ikon View history
12. Tekan tombol Esc pada keyboard
13. Verifikasi modal Changelog tertutup
14. Verifikasi Tab "Preferences" tampil tanpa perubahan

### TC-FA-PREF-294: Klik area di luar modal Changelog tidak menutup modal

15. Klik ikon View history
16. Klik area backdrop gelap di luar modal
17. Verifikasi modal "Changelog: Preferences" tetap terbuka
18. Klik ikon [✕] di header modal

### TC-FA-PREF-297: Modal Changelog tanpa entri menampilkan empty state

19. Atur Changelog Preferences company menjadi tanpa entri (PB-C0) lewat seed hingga tersimpan
20. Muat ulang halaman dengan F5
21. Klik ikon View history
22. Verifikasi empty state menampilkan ilustrasi, judul "No changelog yet", dan deskripsi "Activities and changes will appear here."
23. Klik ikon [✕] di header modal
24. Pulihkan Changelog Preferences company ke 9 entri contoh PB-C1 lewat seed hingga tersimpan

## Notes

- Langkah penghubung (S-03, S-09): modal dibuka pada langkah 1 dan dipakai bersama TC-FA-PREF-27 dan 28 (langkah "Buka Tab Preferences" dan "Klik ikon View history" TC-FA-PREF-28 dipenuhi langkah 1; layar Preferences dibuka hook `beforeEach` suite) dan langkah 8 adalah klik [✕] TC-FA-PREF-292 sekaligus penutup modal sebelum TC berikutnya; langkah 19, 20, dan 24 (mengatur dan memulihkan Changelog kosong); langkah 18 dan 23 (menutup modal).
- Langkah 9 dan 13 (modal tertutup) dan langkah 10 dan 14 mengikuti Expected TC; asersi "tidak ada perubahan" pada Tab "Preferences" dibatasi pada Tab tampil.
- Langkah 11 dan 15 (membuka modal kembali) adalah precondition TC-FA-PREF-293 dan 294.
- Temuan untuk QA:
  - TC-FA-PREF-27 Expected b ("baris pertama" dan "baris terakhir") bergantung pada Changelog yang tepat berisi 9 entri seed; Changelog adalah audit trail permanen yang tumbuh karena Save pada spec lain (S-12, S-14). Spec memakai asumsi bahwa seed PA-17 dan PB-C1 mereset Changelog company seed ke tepat 9 entri (seed terisolasi menurut Catatan TC); bila reset tidak tersedia, Expected perlu ditulis ulang relatif atau dibatasi Filter Date pada tanggal seed.
  - TC-FA-PREF-292, 293, dan 294 Expected "Tab Preferences tampil tanpa perubahan" tidak merinci apa yang dibandingkan; spec mengasersi Tab "Preferences" tampil.
  - TC-FA-PREF-27 dan 28 memakai seri PA sedangkan TC-FA-PREF-292, 293, 294, dan 297 memakai seri PB; spec mengasumsikan nilai awal keduanya setara.
  - TC-FA-PREF-297 tidak menyebut cara memuat ulang modal sesudah Changelog dikosongkan; spec memakai muat ulang halaman.

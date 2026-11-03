---
id: TC-FA-CF-E2E-172-bulk-seluruh-field-dihapus-aktor-lain-saat-aksi
title: "Bulk Activate dan Bulk Delete: Seluruh Field Terpilih Dihapus Aktor Lain Saat Aksi dan Toast Tidak Tersedia"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-342
  - TC-FA-CF-356
coverage:
  web: automated
---

# Bulk Activate dan Bulk Delete: Seluruh Field Terpilih Dihapus Aktor Lain Saat Aksi dan Toast Tidak Tersedia

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini menghapus field milik sendiri di Company Alpha dan membaca log permanen yang dibagi suite.
- Akun aktor sesi 1 (UI): Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson, Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Akun aktor sesi 2 (API, pelaku kedua yang hanya memicu perubahan state): Total Control sesi 2 (Pre-setup #10, pengguna Rina Putri) `totalControlSecond_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC2_PASSWORD`; memakai sesi API aktor yang tidak dihitung sebagai sesi web (lihat `suite.md`). Password tidak ditulis di spec atau fixture.
- Data baseline Company Alpha (Pre-setup #11 dan #12): delapan field tab General tidak diubah spec ini. Hook `before` memulihkan baseline lewat seed reset Company (disediakan tim FE/BE; fixture baru `Fixture.faCustomFields.baseline`).
- Data Dinamis (di-seed lewat API di hook `before`, bersuffix per run; baseline log nol karena nama unik): `Gone Act A {runId}-172` dan `Gone Act B {runId}-172` (Text, Inactive; TC-FA-CF-342), `Gone Del A {runId}-172` dan `Gone Del B {runId}-172` (Text, Active; TC-FA-CF-356). Dengan empat field ini tabel memuat dua belas baris sehingga baris target ditemukan lewat Search. Cleanup: hook `after` menghapus field bersuffix `{runId}-172` yang masih ada lewat API tanpa mengandalkan seeding berhasil penuh.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor sesi 1 dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: Bulk Delete field oleh sesi API aktor kedua dalam satu permintaan; Search tabel Custom Fields; membaca Modal Changelog, Activity Log (Reports & Logs > Activity Log > Tab User Action), serta System Log `Rina Putri` dan `Sarah Johnson` (Settings > User > Detail pengguna > Tab System Log) dengan kata kunci nama field; menunggu toast lama hilang otomatis.
- State global: tidak ada yang diubah selain data field di atas dan flag Guided Tooltip (dipulihkan hook `after`).

## Test Steps

### TC-FA-CF-342: Bulk Activate saat seluruh field terpilih sudah dihapus aktor lain

1. Ketik Search `Gone Act`, tekan Enter
2. Centang baris `Gone Act A {runId}-172` dan `Gone Act B {runId}-172`
3. Hapus `Gone Act A {runId}-172` dan `Gone Act B {runId}-172` lewat sesi API Rina Putri dalam satu permintaan (Bulk Delete) hingga keduanya terhapus tersimpan
4. Klik `[Activate]` pada Bulk Action Bar
5. Klik `[Activate]` pada dialog
6. Verifikasi toast netral `This custom field is no longer available.` tampil
7. Verifikasi tidak ada toast sukses
8. Verifikasi seleksi di-reset

### TC-FA-CF-356: Bulk Delete saat seluruh field terpilih sudah dihapus aktor lain

9. Tunggu toast dari langkah 6 hilang otomatis
10. Ganti isi kotak search dengan `Gone Del`, tekan Enter
11. Centang baris `Gone Del A {runId}-172` dan `Gone Del B {runId}-172`
12. Hapus `Gone Del A {runId}-172` dan `Gone Del B {runId}-172` lewat sesi API Rina Putri dalam satu permintaan (Bulk Delete) hingga keduanya terhapus tersimpan
13. Klik `[Delete]` pada Bulk Action Bar
14. Klik `[Delete]` pada dialog
15. Verifikasi toast netral `This custom field is no longer available.` tampil
16. Verifikasi tidak ada toast sukses
17. Verifikasi seleksi di-reset

### Pembacaan log untuk TC-FA-CF-342 dan TC-FA-CF-356

18. Klik icon Changelog
19. Ketik Search `{runId}-172` pada Modal Changelog, tekan Enter
20. Verifikasi Modal Changelog memuat dua entri Action `Bulk Delete` (satu per field) untuk `Gone Act A {runId}-172` dan `Gone Act B {runId}-172` dari sesi 2
21. Verifikasi Modal Changelog tidak memuat entri Action `Activate` untuk `Gone Act A {runId}-172` maupun `Gone Act B {runId}-172`
22. Verifikasi Modal Changelog memuat dua entri Action `Bulk Delete` (satu per field) untuk `Gone Del A {runId}-172` dan `Gone Del B {runId}-172` dari sesi 2
23. Verifikasi Modal Changelog tidak memuat entri dari klik sesi 1 untuk `Gone Del A {runId}-172` maupun `Gone Del B {runId}-172`
24. Tutup modal Changelog dengan `✕`
25. Buka Activity Log (Reports & Logs > Activity Log > Tab User Action)
26. Cari entri dengan kata kunci `{runId}-172`
27. Verifikasi Activity Log memuat dua entri Action `Bulk Delete` (satu per field) untuk `Gone Act A {runId}-172` dan `Gone Act B {runId}-172` dari sesi 2
28. Verifikasi Activity Log tidak memuat entri Action `Activate` untuk `Gone Act A {runId}-172` maupun `Gone Act B {runId}-172`
29. Verifikasi Activity Log memuat dua entri Action `Bulk Delete` (satu per field) untuk `Gone Del A {runId}-172` dan `Gone Del B {runId}-172` dari sesi 2
30. Verifikasi Activity Log tidak memuat entri dari klik sesi 1 untuk `Gone Del A {runId}-172` maupun `Gone Del B {runId}-172`
31. Buka System Log `Rina Putri` (sesi 2)
32. Cari entri dengan kata kunci `{runId}-172`
33. Verifikasi System Log `Rina Putri` memuat dua entri Action `Bulk Delete` untuk `Gone Act A {runId}-172` dan `Gone Act B {runId}-172`
34. Verifikasi System Log `Rina Putri` memuat dua entri Action `Bulk Delete` untuk `Gone Del A {runId}-172` dan `Gone Del B {runId}-172`
35. Buka System Log `Sarah Johnson` (sesi 1)
36. Cari entri dengan kata kunci `{runId}-172`
37. Verifikasi System Log `Sarah Johnson` tidak memuat entri untuk `Gone Act A {runId}-172` maupun `Gone Act B {runId}-172`
38. Verifikasi System Log `Sarah Johnson` tidak memuat entri untuk `Gone Del A {runId}-172` maupun `Gone Del B {runId}-172`

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 342 lalu 356; sama dengan urutan TC sumber. Pembacaan keempat surface log dilakukan sekali sesudah kedua TC (langkah 18 sampai 38) dan bukan sesudah tiap TC, karena entri log tiap TC unik per nama field bersuffix `{runId}-172` (baseline nol; S-12) dan tidak saling mengganggu; pemisahan pembacaan per TC menggandakan navigasi dan pembacaan surface yang sama.
- Spec berada di sekitar 35 langkah (38 langkah). Seluruhnya satu topik (Bulk Activate dan Bulk Delete saat seluruh field terpilih sudah dihapus aktor lain) dan satu dataset milik spec; 21 langkah adalah pembacaan empat surface log yang dipakai bersama oleh dua TC.
- P-1: klausa "tidak ada entri Activate" TC-FA-CF-342 dan "tidak ada entri dari klik sesi 1" TC-FA-CF-356 (langkah 21, 23, 28, 30, 37, dan 38) menempel pada state konflik yang dibangun alur ini (seluruh field terpilih dihapus sesi 2 saat dialog sesi 1 akan dikonfirmasi) dan diasersi pada nama field bersuffix unik `{runId}-172` dengan baseline nol (S-12); tidak ada spec absence yang memuat aksi nyata untuk TC ini (S-05). Anchor positif (8b butir 2): toast netral (langkah 6 dan 15) serta entri Action `Bulk Delete` dari sesi 2 pada surface yang sama (langkah 20, 22, 27, 29, 33, dan 34).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 10 (Search agar baris target tampil), langkah 3 dan 12 (pemicu pelaku kedua lewat sesi API), langkah 9 (menunggu toast netral lama hilang otomatis supaya toast pada langkah 15 adalah toast hasil langkah 14), langkah 18, 25, 31, dan 35 (membuka surface log), langkah 19, 26, 32, dan 36 (mencari entri), dan langkah 24 (menutup modal Changelog).
- Asersi tambahan di luar Expected TC (S-03): langkah 7 dan 16 menurunkan "tanpa toast sukses" menjadi `Verifikasi` terpisah dengan anchor toast netral pada langkah 6 dan 15; langkah 31 sampai 34 (System Log `Rina Putri`) dibaca sebelum System Log `Sarah Johnson` agar mekanisme pencarian log terbukti menampilkan entri sebelum asersi absence pada langkah 37 dan 38.
- Data milik spec (S-06, S-12): TC-FA-CF-342 dan TC-FA-CF-356 menyebut field Inactive acak dan `Legacy Tag` serta `Compliance File`; spec memakai field Dinamis bersuffix `{runId}-172` agar entri log dapat diasersi dari baseline nol tanpa menghapus field Pre-setup bersama.
- Pelaku kedua (Rina Putri) memakai sesi API karena hanya memicu perubahan state (Bulk Delete); tidak membuka sesi UI kedua dan tidak memakai `P-2`.
- Temuan untuk QA:
  - TC-FA-CF-342 langkah 1 hanya menyebut "dua field Inactive" tanpa nama; spec memakai field Dinamis `Gone Act A` dan `Gone Act B`.
  - TC-FA-CF-342 dan TC-FA-CF-356 tidak menyebut kolom atau cara mengenali "dari sesi 2" dan "dari klik sesi 1" pada Changelog dan Activity Log, maupun cara mencari entri pada Activity Log dan System Log; spec memakai asal aksi (sesi) dan kata kunci nama field.
  - TC-FA-CF-342 Expected butir b "tidak ada mutasi" atas field yang sudah terhapus tidak punya cara pengamatan terpisah di UI; tercakup oleh ketiadaan entri Activate (langkah 21, 28) dan toast netral (langkah 6).
  - Email akun Total Control sesi 2 (Pre-setup #10) mengikuti pola Pre-setup; env `FA_TC2_PASSWORD` disediakan tim FE.

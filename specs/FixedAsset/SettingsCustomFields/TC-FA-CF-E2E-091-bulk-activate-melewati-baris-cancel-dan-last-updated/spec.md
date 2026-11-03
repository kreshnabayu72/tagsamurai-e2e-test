---
id: TC-FA-CF-E2E-091-bulk-activate-melewati-baris-cancel-dan-last-updated
title: "Bulk Activate dan Deactivate: Cancel Mempertahankan Seleksi, Baris Dilewati Tanpa Entri Log, dan Last Updated"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-336
  - TC-FA-CF-337
  - TC-FA-CF-630
  - TC-FA-CF-635
coverage:
  web: automated
---

# Bulk Activate dan Deactivate: Cancel Mempertahankan Seleksi, Baris Dilewati Tanpa Entri Log, dan Last Updated

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): blok terakhir (TC-FA-CF-336 dan TC-FA-CF-635) mengaktifkan field baseline Company Alpha, dan spec membaca log permanen yang dibagi suite.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson, Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data baseline Company Alpha (Pre-setup #11 dan #12), tab General delapan baris dalam satu halaman: `Asset Serial Tag` (Active, Modified By `Budi S`, Last Updated `17/10/26, 10:45`), `Legacy Tag` (Active), `Depreciated Ratio` (Inactive), dan `Compliance File` (dinonaktifkan lewat seed API di hook `before`, sehingga Inactive; precondition TC-FA-CF-630). Hook `before` memulihkan baseline lewat seed reset Company (disediakan tim FE/BE; fixture baru `Fixture.faCustomFields.baseline`). Spec ini mengaktifkan `Depreciated Ratio` (langkah 29) sehingga Last Updated dan Modified By-nya berubah sampai seed reset berikutnya; hook `after` memulihkan.
- Format tanggal: General Settings Company Alpha `dd/MM/yy` dan 24 jam (Pre-setup #11); jam server dan jam browser sinkron untuk asersi Last Updated (toleransi satu menit).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: membaca jumlah entri Modal Changelog, System Log aktor (Settings > User > Detail pengguna aktor > Tab System Log), dan Activity Log (Reports & Logs > Activity Log > Tab User Action) sebagai baseline (disediakan tim FE/BE; audit trail permanen sehingga hanya selisih terhadap baseline yang diasersi); seeding status `Compliance File` Inactive lewat API (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain status `Depreciated Ratio` dan flag Guided Tooltip (dipulihkan hook `after`).

## Test Steps

### Baseline log

1. Catat jumlah entri awal pada Modal Changelog, System Log aktor, dan Activity Log sebagai baseline (aksi baca tanpa `Verifikasi`)

### TC-FA-CF-337: Cancel pada dialog Bulk Deactivate

2. Centang baris `Asset Serial Tag` dan `Legacy Tag`
3. Klik `[Deactivate]` pada Bulk Action Bar
4. Klik `[Cancel]` pada dialog
5. Verifikasi dialog tertutup
6. Verifikasi seleksi `Asset Serial Tag` dan `Legacy Tag` dipertahankan
7. Verifikasi Bulk Action Bar dipertahankan
8. Verifikasi tidak ada perubahan data: switch Active baris `Asset Serial Tag` dan `Legacy Tag` tetap ON
9. Klik icon `[✕]` pada Bulk Action Bar

### TC-FA-CF-630: Cancel pada dialog Bulk Activate

10. Centang baris `Depreciated Ratio` dan `Compliance File`
11. Klik `[Activate]` pada Bulk Action Bar
12. Klik `[Cancel]` pada dialog
13. Verifikasi dialog `Activate Custom Fields` tertutup
14. Verifikasi seleksi `Depreciated Ratio` dan `Compliance File` dipertahankan
15. Verifikasi Bulk Action Bar dipertahankan
16. Verifikasi status kedua field tetap Inactive
17. Verifikasi tidak ada toast
18. Klik icon `[✕]` pada Bulk Action Bar

### Pembacaan log untuk TC-FA-CF-337 dan TC-FA-CF-630

19. Klik icon Changelog
20. Verifikasi jumlah entri Modal Changelog sama dengan baseline langkah 1 (tidak ada entri dari langkah 4 dan 12)
21. Tutup modal Changelog dengan `✕`
22. Buka System Log aktor (Settings > User > Detail pengguna aktor > Tab System Log)
23. Verifikasi jumlah entri System Log aktor sama dengan baseline langkah 1 (tidak ada entri dari langkah 4 dan 12)
24. Buka Activity Log (Reports & Logs > Activity Log > Tab User Action)
25. Verifikasi jumlah entri Activity Log sama dengan baseline langkah 1 (tidak ada entri dari langkah 4 dan 12)
26. Buka Fixed Asset > Settings > Custom Fields (tab General)

### TC-FA-CF-336 dan TC-FA-CF-635: Bulk Activate pada seleksi campuran melewati baris yang sudah Active

27. Centang baris `Asset Serial Tag` (Active) dan `Depreciated Ratio` (Inactive)
28. Klik `[Activate]` pada Bulk Action Bar
29. Klik `[Activate]` pada dialog
30. Verifikasi toast sukses `Success, custom field has been activated.` tampil tanpa varian partial
31. Verifikasi switch Active baris `Depreciated Ratio` berada di posisi ON
32. Verifikasi switch Active baris `Asset Serial Tag` tetap ON
33. Verifikasi baris `Asset Serial Tag` tetap menampilkan Modified By `Budi S` dan Last Updated `17/10/26, 10:45`
34. Verifikasi baris `Depreciated Ratio` menampilkan Modified By `Sarah J` dan Last Updated waktu aksi (toleransi satu menit)
35. Klik icon Changelog
36. Verifikasi jumlah entri Modal Changelog bertambah tepat satu dibanding baseline langkah 1
37. Verifikasi entri baru itu Action `Activate` untuk `Depreciated Ratio` dan tidak ada entri baru untuk `Asset Serial Tag`
38. Tutup modal Changelog dengan `✕`

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (38 langkah). Seluruhnya satu topik (dialog konfirmasi Bulk Activate dan Deactivate yang dibatalkan atau melewati baris) pada satu dataset baseline Company Alpha; tiga blok berdiri sendiri, dan tujuh langkah pembacaan log (langkah 19 sampai 25) dipakai bersama oleh dua TC Cancel.
- Urutan TC dalam spec: 337 dan 630 (Cancel tanpa mutasi), pembacaan log, lalu 336 dan 635 (aksi yang mengubah data, paling akhir; S-10). Urutan menyimpang dari urutan TC sumber (336, 337, 630, 635) agar baseline log (langkah 1) belum terpengaruh tulisan log dari TC-FA-CF-336. Aksi TC-FA-CF-336 dan TC-FA-CF-635 identik (langkah 27 sampai 29) sehingga dijalankan sekali.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (baseline log), langkah 9 dan 18 (membersihkan seleksi; S-09), langkah 19, 22, dan 24 (membuka surface log), langkah 21 dan 38 (menutup modal Changelog), dan langkah 26 (kembali ke layar Custom Fields, yang juga membersihkan seleksi).
- P-1: asersi "tidak ada entri log" TC-FA-CF-337 dan TC-FA-CF-630 (langkah 20, 23, dan 25) serta "baris yang dilewati tidak menulis entri" TC-FA-CF-336 (langkah 36 dan 37) berada di spec ini karena bergantung pada state dialog Cancel dan seleksi campuran yang dibangun spec ini; dipenuhi dengan baseline jumlah entri (langkah 1; S-12), bukan posisi baris teratas.
- Asersi tambahan di luar Expected TC (S-03): langkah 36 dan 37 menurunkan "hanya satu entri Activate tercatat (untuk `Depreciated Ratio`)" TC-FA-CF-336 butir c menjadi selisih jumlah entri satu terhadap baseline dan identitas entri baru; langkah 14 dan 15 memecah "seleksi dan Bulk Action Bar dipertahankan" menjadi dua `Verifikasi`.
- Temuan untuk QA:
  - TC-FA-CF-337 Expected "tidak ada perubahan data atau log" tidak menyebut surface log yang dibuka; spec memakai tiga surface sesuai langkah 3 TC (Modal Changelog, System Log aktor, Activity Log).
  - TC-FA-CF-630 mensyaratkan `Compliance File` Inactive lewat seed API padahal baseline Pre-setup #12 menyebutnya Active; spec men-seed status itu di hook `before`.
  - TC-FA-CF-336 butir a ("tanpa varian partial") ditulis sebagai teks toast persis tanpa kalimat `Some items were skipped.`; tidak ada asersi absence terpisah.
  - TC-FA-CF-635 mengasersi waktu aksi pada Last Updated tanpa menyebut toleransi; spec memakai toleransi satu menit (S-12).

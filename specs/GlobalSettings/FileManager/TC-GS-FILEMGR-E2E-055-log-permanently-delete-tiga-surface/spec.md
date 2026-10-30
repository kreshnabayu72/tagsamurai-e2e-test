---
id: TC-GS-FILEMGR-E2E-055-log-permanently-delete-tiga-surface
title: "Pencatatan Log Permanently Delete Single dan Bulk di Changelog File Manager, System Log, dan Activity Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-223
  - TC-GS-FILEMGR-224
  - TC-GS-FILEMGR-234
coverage:
  web: automated
---

# Pencatatan Log Permanently Delete Single dan Bulk di Changelog File Manager, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani (`Sinta M`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`). Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Data milik spec (suffix `{runId}-055`, seeding lewat fixture BE di hook `before`; mekanisme seeding tidak didefinisikan di TC, disediakan tim FE/BE):
  - `old-avatar-{runId}-055.png` di Recycle Bin, Deleted By Sinta Maharani (salinan R01), dipakai TC-223.
  - `recycled-photo-01-{runId}-055.jpg`, `recycled-photo-02-{runId}-055.jpg`, `recycled-photo-03-{runId}-055.jpg` (salinan R05 sampai R07) di Recycle Bin, dipakai TC-224. `recycled-photo-04-{runId}-055.jpg` (salinan R08) di Recycle Bin sebagai file yang tidak dipilih (pembanding Expected d TC-224).
  - `recycled-photo-10-{runId}-055.jpg` dan `recycled-photo-11-{runId}-055.jpg` (salinan R14 dan R15) di Recycle Bin, dipakai TC-234.
- Kemampuan teknis (disediakan tim FE/BE): sesi API pelaku lain yang menghapus permanen `recycled-photo-11-{runId}-055.jpg` sebagai pemicu TC-234 (bukan objek asersi).
- Baseline log: semua nama file bersuffix unik per run, sehingga jumlah entri awal di tiap surface log adalah nol dan asersi "tepat N baris" dihitung terhadap pencarian nama bersuffix.
- Dependensi TC (TC-90, TC-100, TC-101: Permanently Delete single, bulk, dan bulk dengan item dilewati) dijalankan sebagai langkah aksi di spec ini.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus permanen lewat API sisa file bersuffix `{runId}-055` yang masih ada di Recycle Bin.
- Tidak ada state global yang diubah.

## Test Steps

### TC-GS-FILEMGR-223: Log Permanently Delete single di tiga surface

1. Klik tombol Recycle Bin di toolbar
2. Ketik Search `old-avatar-{runId}-055`, tekan Enter
3. Klik ikon (⋯) baris `old-avatar-{runId}-055.png`, klik `Permanently Delete`, lalu klik [Permanently Delete]
4. Tunggu aksi selesai
5. Tutup modal Recycle Bin lewat `✕`, klik ikon Changelog di toolbar
6. Ketik Search `old-avatar-{runId}-055`, tekan Enter
7. Verifikasi Changelog File Manager: tepat satu baris dengan Action `Permanently Delete`, File Name `old-avatar-{runId}-055.png`, Field `File Name`, Old Value `old-avatar-{runId}-055.png`, New Value `—`, Modified By `Sinta M`
8. Tutup modal Changelog lewat `✕`, buka Global Settings > User > Detail User Sinta Maharani > tab System Log
9. Ketik Search `old-avatar-{runId}-055`, tekan Enter
10. Verifikasi System Log Detail User Sinta Maharani: tepat satu baris dengan Action `Permanently Delete`, Object `File Manager`, Name `old-avatar-{runId}-055.png`, Field `File Name`, Old Value `old-avatar-{runId}-055.png`, New Value `—`
11. Buka Global Settings > Activity Log, ketik Search `old-avatar-{runId}-055`, tekan Enter
12. Verifikasi Activity Log: tepat satu baris dengan Action `Permanently Delete`, Object `File Manager`, Name `old-avatar-{runId}-055.png`, Field `File Name`, Old Value `old-avatar-{runId}-055.png`, New Value `—`, Modified By `Sinta M`
13. Buka Global Settings > File Manager

### TC-GS-FILEMGR-224: Satu entri log per file pada Permanently Delete bulk

14. Klik tombol Recycle Bin di toolbar, ketik Search `-{runId}-055.jpg`, tekan Enter
15. Centang baris `recycled-photo-01-{runId}-055.jpg`, `recycled-photo-02-{runId}-055.jpg`, dan `recycled-photo-03-{runId}-055.jpg`
16. Klik `Bulk Action`, klik `Permanently Delete`, lalu klik [Permanently Delete]
17. Tunggu aksi selesai
18. Tutup modal Recycle Bin lewat `✕`, klik ikon Changelog di toolbar, ketik Search `-{runId}-055.jpg`, tekan Enter
19. Verifikasi Changelog: tepat tiga baris Action `Permanently Delete`, satu per file untuk `recycled-photo-01-{runId}-055.jpg`, `recycled-photo-02-{runId}-055.jpg`, dan `recycled-photo-03-{runId}-055.jpg`
20. Verifikasi Modified By `Sinta M` pada ketiga baris Changelog
21. Verifikasi Changelog tidak memuat baris untuk `recycled-photo-04-{runId}-055.jpg`
22. Tutup modal Changelog lewat `✕`, buka Detail User Sinta Maharani > tab System Log, ketik Search `-{runId}-055.jpg`, tekan Enter
23. Verifikasi System Log Sinta Maharani: tepat tiga baris Action `Permanently Delete` untuk ketiga file
24. Buka Global Settings > Activity Log, ketik Search `-{runId}-055.jpg`, tekan Enter
25. Verifikasi Activity Log: tepat tiga baris Action `Permanently Delete` untuk ketiga file
26. Verifikasi Modified By `Sinta M` pada ketiga baris Activity Log
27. Buka Global Settings > File Manager

### TC-GS-FILEMGR-234: Item bulk yang dilewati tidak menulis entri log

28. Klik tombol Recycle Bin di toolbar, ketik Search `-{runId}-055.jpg`, tekan Enter
29. Centang baris `recycled-photo-10-{runId}-055.jpg` dan `recycled-photo-11-{runId}-055.jpg`
30. Klik `Bulk Action`, klik `Permanently Delete` sehingga dialog konfirmasi tampil
31. Hapus permanen `recycled-photo-11-{runId}-055.jpg` lewat sesi API pelaku lain hingga tersimpan
32. Klik [Permanently Delete] pada dialog
33. Verifikasi toast sukses: "Success, file has been permanently deleted. Some items were skipped."
34. Tutup modal Recycle Bin lewat `✕`, klik ikon Changelog di toolbar
35. Ketik Search `recycled-photo-10-{runId}-055.jpg`, tekan Enter
36. Verifikasi Changelog: tepat satu baris untuk `recycled-photo-10-{runId}-055.jpg`
37. Ganti isi kotak search dengan `recycled-photo-11-{runId}-055.jpg`, tekan Enter
38. Verifikasi Changelog tidak memuat baris untuk `recycled-photo-11-{runId}-055.jpg` (empty state "No results found")
39. Tutup modal Changelog lewat `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Kelas pencatatan (log tiga surface).
- Urutan TC di spec sama dengan urutan sumber (223, 224, 234); semuanya Permanently Delete atas data milik spec, sehingga tidak ada kasus lain yang kehilangan baris.
- Spec berjumlah 39 langkah nominal. Blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung ke batas sekitar 35 langkah (konvensi bagian 3, smell); langkah di luar blok itu kurang dari 25. Semua blok satu kelas (pencatatan Permanently Delete), berdiri sendiri, dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Data TC memakai nama Pre-setup literal (`old-avatar.png`, `recycled-photo-01.jpg`, dan seterusnya). Spec memakai salinan bersuffix milik spec karena target aksi tulis tidak boleh data Pre-setup bersama (S-06) dan kecocokan "tepat N baris" bergantung pada nama unik (S-12). Pencarian `-{runId}-055.jpg` dipakai agar hanya baris spec ini yang terhitung.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 4 dan 17 (Tunggu aksi selesai sebelum pindah surface), langkah 5, 8, 18, 22, 34, 39 (menutup modal), langkah 13 dan 27 (kembali ke File Manager), langkah 2, 14, 28 (Search nama bersuffix pada Recycle Bin), langkah 15 dan 29 (mencentang baris target), dan langkah 31 (pemicu proses lain, TC sumber hanya menyebut "dihapus permanen oleh proses lain sebelum Confirm"; urutan dialog dibuka dahulu, proses lain menghapus, lalu Confirm mengikuti S-04).
- Asersi di System Log dan Activity Log TC-224 butir d ("tidak ada entri untuk file lain yang tidak terpilih") diasersi pada Changelog (langkah 21); TC sumber tidak menyebut surface untuk butir ini.
- Asersi "tidak ada baris untuk `recycled-photo-11`" (langkah 38) memakai baseline nol karena nama bersuffix unik, dengan anchor positif baris `recycled-photo-10` pada langkah 36 dan toast pada langkah 33. Keputusan D-1 (opsi B): klausa absence tetap di spec asal tanpa spec absence terpisah; P-1 (state berat: item dihapus proses lain pada langkah 31 dibangun sebelum Confirm dan tidak bisa diulang tanpa seeding berat).
- Temuan untuk QA:
  - Mekanisme seeding file, Recycle Bin, dan pemicu "dihapus oleh proses lain" tidak didefinisikan di TC (Q-4, Q-8); ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa mengarang endpoint.
  - TC-224 Post Condition dan Expected tidak menyebut surface untuk butir d (lihat catatan di atas).

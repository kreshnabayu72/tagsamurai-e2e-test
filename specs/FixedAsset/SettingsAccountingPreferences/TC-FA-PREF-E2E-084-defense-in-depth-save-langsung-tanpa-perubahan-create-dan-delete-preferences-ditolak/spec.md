---
id: TC-FA-PREF-E2E-084-defense-in-depth-save-langsung-tanpa-perubahan-create-dan-delete-preferences-ditolak
title: "Defense-in-depth: Save Langsung Tanpa Perubahan Nilai Berhasil, Create dan Delete Preferences oleh User Ditolak Server"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-232
  - TC-FA-PREF-544
  - TC-FA-PREF-545
coverage:
  web: automated
---

# Defense-in-depth: Save Langsung Tanpa Perubahan Nilai Berhasil, Create dan Delete Preferences oleh User Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Kelas harness: a (defense-in-depth, request langsung ke server).
- Akun aktor: Total Control (Pre-setup PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PB-1 untuk TC-FA-PREF-232 dan PC-1 untuk TC-FA-PREF-544 dan TC-FA-PREF-545 (setara: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date); akun Chart of Accounts PB-2 (`4-9100 – Laba Pelepasan Aset`, Active, function Gain on Disposal); Changelog Preferences berisi 1 entri Create. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API); seed ulang ke nilai awal dilakukan lewat langkah penghubung (langkah 7).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): request langsung ke server memakai sesi API Total Control Rina Anggraini (butir "Sesi API aktor" di `suite.md`); fixture BE untuk mengubah status akun Chart of Accounts dan membaca ulang Preferences; kemampuan baca BE jumlah baris Changelog Preferences, jumlah entri System Log Rina Anggraini, dan jumlah entri Activity Log FAMS (dipakai sebagai baseline, bagian 8b butir 10).
- State yang diubah spec: status akun `4-9100 – Laba Pelepasan Aset` (Inactive pada langkah 1) dan Default Gain on Disposal; dipulihkan pada langkah 7 dan di hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-232: Request langsung tanpa perubahan tidak mengevaluasi validasi nilai meski akun tersimpan Inactive

1. Set Default Gain on Disposal tersimpan "4-9100 – Laba Pelepasan Aset" lalu ubah status akun itu menjadi Inactive lewat fixture BE hingga tersimpan
2. Kirim request langsung Save Preferences memakai sesi API Total Control Rina Anggraini, berisi seluruh nilai yang sama persis dengan nilai tersimpan termasuk akun "4-9100 – Laba Pelepasan Aset" yang Inactive
3. Verifikasi server membalas sukses 200
4. Verifikasi respons tidak memuat galat validasi V-04
5. Baca ulang Preferences lewat fixture BE
6. Verifikasi seluruh nilai Preferences sama dengan sebelum permintaan
7. Pulihkan status akun "4-9100 – Laba Pelepasan Aset" menjadi Active dan Preferences ke nilai awal PB-1 lewat seed hingga tersimpan

### TC-FA-PREF-544: Request langsung membuat Preferences baru oleh user ditolak

8. Catat jumlah baris Changelog Preferences, jumlah entri System Log Rina Anggraini, dan jumlah entri Activity Log FAMS (baseline)
9. Kirim request langsung pembuatan Preferences baru memakai sesi API Total Control Rina Anggraini
10. Verifikasi server menolak permintaan
11. Baca ulang nilai Preferences tersimpan lewat fixture BE
12. Verifikasi nilai Preferences tersimpan tidak berubah
13. Muat ulang halaman dengan F5
14. Verifikasi Tab "Preferences" aktif
15. Klik ikon View history
16. Verifikasi modal Changelog: Preferences memuat sedikitnya satu baris
17. Verifikasi jumlah baris Changelog sama dengan baseline langkah 8
18. Verifikasi modal Changelog: Preferences tidak memuat baris Action = Create baru
19. Verifikasi jumlah entri System Log Rina Anggraini sama dengan baseline langkah 8
20. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline langkah 8
21. Klik ikon [✕] di header modal Changelog

### TC-FA-PREF-545: Request langsung menghapus Preferences oleh user ditolak

22. Catat jumlah baris Changelog Preferences, jumlah entri System Log Rina Anggraini, dan jumlah entri Activity Log FAMS (baseline)
23. Kirim request langsung penghapusan Preferences memakai sesi API Total Control Rina Anggraini
24. Verifikasi server menolak permintaan
25. Muat ulang halaman dengan F5
26. Verifikasi Tab "Preferences" menampilkan seluruh nilai tersimpan: Fiscal Year Start "January", First Accounting Period "March" "2026", Default Capitalization Threshold "Rp 5.000.000,00", In-service Date Source "Activation date"
27. Verifikasi jumlah baris Changelog sama dengan baseline langkah 22
28. Verifikasi jumlah entri System Log Rina Anggraini sama dengan baseline langkah 22
29. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline langkah 22

## Notes

- K-1: TC-FA-PREF-232, 544, dan 545 adalah TC defense-in-depth (kelas a) yang Expected-nya berupa respons API dan state data; tetap masuk spec FE+BE walau tumpang tindih dengan `tc-[modul]-backend.md` (bagian 3 prinsip 13a).
- Langkah penghubung (S-03, S-09): langkah 7 (memulihkan akun dan Preferences ke nilai awal), langkah 13 (muat ulang agar modal Changelog memuat data terkini), dan langkah 21 (menutup modal). Langkah 14 dan 16 adalah anchor positif sebelum asersi absence (bagian 8b butir 2, R-21) dan merupakan asersi tambahan di luar Expected TC. Layar Preferences dibuka hook `beforeEach` suite, sehingga langkah TC "Buka Settings > Accounting > Preferences" tidak diulang kecuali langkah 25 (muat ulang).
- Langkah 2 sampai 6 dan 9 sampai 12, 23 sampai 24: request langsung ke server hanya mengasersi respons dan state data lewat fixture BE (bagian 8b butir 1). Jumlah baris Changelog, System Log, dan Activity Log pada TC-FA-PREF-544 dan 545 diasersi sebagai selisih terhadap baseline (asersi jumlah, S-12), bukan sebagai asersi absence kelas g.
- TC defense-in-depth pada company tanpa baris Preferences (TC-FA-PREF-276, 562) ada di spec 167.
- Cara baca: jumlah baris Changelog, System Log, dan Activity Log memakai kemampuan baca BE (bagian 8b butir 10); modal Changelog dibuka lewat UI hanya untuk Expected TC-FA-PREF-544 butir c.
- Temuan untuk QA:
  - TC-FA-PREF-232 Expected a menyebut "tanpa caption V-04" pada request langsung; caption adalah elemen UI sehingga spec mengasersi bahwa respons tidak memuat galat validasi V-04 (bagian 8b butir 1). Post Condition butir b ("Tidak ada entri log baru") tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-FA-PREF-544 dan 545 Post Condition ("Company tetap memiliki tepat satu set Preferences") tidak punya langkah observasi di TC dan tidak diasersi terpisah; nilai tersimpan diasersi lewat Expected b.
  - TC-FA-PREF-544 dan 545 tidak menyebut status respons penolakan (hanya "Server menolak permintaan"); spec tidak mengasersi kode status tertentu.
  - Asersi "tidak ada entri log baru" atas penolakan request langsung (TC-FA-PREF-544, 545) ditulis di sini sebagai selisih jumlah terhadap baseline; bila tim menilai S-05 mengharuskannya di spec absence (kelas g), TC ini perlu masuk `sourceTc` spec absence juga.

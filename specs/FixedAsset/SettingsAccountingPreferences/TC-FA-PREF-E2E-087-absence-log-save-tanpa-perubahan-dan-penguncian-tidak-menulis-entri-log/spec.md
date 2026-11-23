---
id: TC-FA-PREF-E2E-087-absence-log-save-tanpa-perubahan-dan-penguncian-tidak-menulis-entri-log
title: "Absence Log: Save Tanpa Perubahan dan Penguncian Tidak Menulis Entri Log"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-231
  - TC-FA-PREF-244
  - TC-FA-PREF-382
  - TC-FA-PREF-602
sourceRules: ["R-02", "F-FAPREF-01.k1a", "F-FAPREF-01.k1b", "FAPREF-LOGIC-03e", "ST-05"]
smoke: []
dependsOn: []
trace:
  "R-02": [3, 21]
  "F-FAPREF-01.k1a": [3, 5, 21, 23]
  "F-FAPREF-01.k1b": [6, 24, 25, 26]
  "FAPREF-LOGIC-03e": 23
  "ST-05": [30, 31]
anchor: [12, 14, 15, 32, 33, 34]
coverage:
  web: automated
---

# Absence Log: Save Tanpa Perubahan dan Penguncian Tidak Menulis Entri Log

## Prerequisites

- Mode: FE+BE.
- Kelas harness: g (asersi absence log). Pemicu (request langsung ke server dan penguncian lewat fixture BE) hanya membentuk kondisi yang diasersi tidak tercatat (P-5).
- Akun aktor: Total Control (Pre-setup PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PB-1 untuk TC-FA-PREF-231 dan TC-FA-PREF-244 dan PC-1 untuk TC-FA-PREF-382 dan TC-FA-PREF-602 (setara: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date; belum ada Run Posted); akun Chart of Accounts PB-2; Asset Class IT Equipment (PB-3 dan PC-6); Changelog Preferences berisi 1 entri Create (PB-1). Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API); seed ulang ke nilai awal dilakukan lewat langkah penghubung (langkah 17, 18, dan 35).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): request langsung ke server memakai sesi API Total Control Rina Anggraini (butir "Sesi API aktor" di `suite.md`) dan fixture BE untuk membaca ulang Preferences; fixture BE untuk menandai posting penyusutan pertama pada Asset Class IT Equipment (Last Posted Period Apr 2026); kemampuan baca BE jumlah baris Changelog Preferences, jumlah entri System Log Rina Anggraini, dan jumlah entri Activity Log FAMS (baseline sebelum aksi, bagian 8b butir 10 dan S-12).
- State yang diubah spec: posting penyusutan pertama Asset Class IT Equipment (langkah 10 dan 28), dipulihkan pada langkah 17 dan 35 dan di hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-231: Permintaan langsung Save tanpa perubahan nilai berhasil tanpa mutasi dan tanpa log

1. Catat jumlah baris Changelog Preferences (baseline)
2. Kirim request langsung Save Preferences memakai sesi API Total Control Rina Anggraini, berisi seluruh nilai yang sama persis dengan nilai tersimpan
3. Verifikasi server membalas sukses 200
4. Baca ulang Preferences lewat fixture BE
5. Verifikasi seluruh nilai Preferences sama dengan sebelum permintaan
6. Verifikasi jumlah baris Changelog sama dengan baseline langkah 1

### TC-FA-PREF-244: Penguncian tidak menulis entri log tersendiri pada Changelog Preferences

7. Klik ikon View history
8. Catat jumlah baris pada modal Changelog (baseline)
9. Klik ikon [✕] di header modal Changelog
10. Tandai posting penyusutan pertama pada Asset Class IT Equipment lewat fixture BE hingga tersimpan
11. Muat ulang halaman dengan F5
12. Verifikasi Tab "Preferences" aktif
13. Klik ikon View history
14. Verifikasi jumlah baris pada modal Changelog sama dengan baseline langkah 8 (1 baris)
15. Verifikasi tidak ada baris dengan Field Fiscal Year Start atau First Accounting Period yang menyatakan penguncian
16. Klik ikon [✕] di header modal Changelog
17. Pulihkan Preferences dan Asset Class ke nilai awal PB-1 (tanpa posting penyusutan) lewat seed hingga tersimpan

### TC-FA-PREF-382: Request langsung Save tanpa perubahan nilai berhasil tanpa mutasi dan tanpa log

18. Seed ulang Preferences ke nilai awal PC-1 hingga tersimpan
19. Catat jumlah baris Changelog Preferences, jumlah entri System Log Rina Anggraini, dan jumlah entri Activity Log FAMS (baseline)
20. Kirim request langsung Save Preferences memakai klien HTTP dengan sesi API Rina Anggraini, berisi seluruh setting bernilai sama dengan nilai tersimpan
21. Verifikasi respons server 200
22. Muat ulang halaman dengan F5
23. Verifikasi Form Preferences memuat nilai tersimpan yang tidak berubah: Fiscal Year Start "January", First Accounting Period "March" "2026", Default Capitalization Threshold "Rp 5.000.000,00", In-service Date Source "Activation date"
24. Verifikasi jumlah baris Changelog sama dengan baseline langkah 19
25. Verifikasi jumlah entri System Log Rina Anggraini sama dengan baseline langkah 19
26. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline langkah 19

### TC-FA-PREF-602: Kunci Fiscal Year Start dan First Accounting Period tidak dicatat sebagai entri log

27. Catat jumlah baris Changelog Preferences, jumlah entri System Log Rina Anggraini, dan jumlah entri Activity Log FAMS (baseline)
28. Lakukan posting penyusutan pertama sehingga Depreciation Run periode Apr 2026 berstatus Posted (Asset Class IT Equipment memiliki Last Posted Period Apr 2026) lewat fixture BE hingga tersimpan
29. Muat ulang halaman dengan F5
30. Verifikasi Fiscal Year Start tampil Disabled dengan ikon gembok
31. Verifikasi First Accounting Period tampil Disabled dengan ikon gembok
32. Verifikasi jumlah baris Changelog sama dengan baseline langkah 27
33. Verifikasi jumlah entri System Log Rina Anggraini sama dengan baseline langkah 27
34. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline langkah 27
35. Pulihkan Preferences dan Asset Class ke nilai awal PC-1 (tanpa posting penyusutan) lewat seed hingga tersimpan

## Notes

- P-5: spec ini adalah spec absence (kelas g); request langsung Save (TC-FA-PREF-231, 382) dan penguncian lewat fixture BE (TC-FA-PREF-244, 602) hanya memicu kondisi yang diasersi tidak tercatat dan bukan objek uji. Tiap TC punya baseline sendiri (S-12, S-05); asersi pencatatan sah untuk Save yang mengubah nilai ada di spec lain.
- Langkah penghubung (S-03, S-09): langkah 9 dan 16 (menutup modal), langkah 17, 18, dan 35 (memulihkan Preferences dan Asset Class ke nilai awal), langkah 11 dan 22 dan 29 (muat ulang agar tampilan memuat state terkini). Langkah 12 adalah anchor positif sebelum asersi absence pada popup yang dibuka sesudah F5 (R-21, bagian 8b butir 2) dan merupakan asersi tambahan di luar Expected TC; baseline yang dicatat dan baris yang ada pada modal menjadi anchor tambahan.
- Cara baca (bagian 8b butir 10): jumlah baris Changelog dibaca lewat kemampuan baca BE kecuali TC-FA-PREF-244 yang menyebut modal Changelog secara eksplisit; setara dengan menghitung baris pada modal View history.
- Temuan untuk QA:
  - TC-FA-PREF-231 dan 244 Post Condition ("Tidak ada entri log baru pada Changelog, System Log, maupun Activity Log") tidak punya langkah observasi untuk System Log dan Activity Log di TC; hanya jumlah baris Changelog yang diasersi (Expected c dan Expected a) dan Post Condition tidak diklaim teruji untuk dua surface lain (S-05).
  - TC-FA-PREF-244 Expected b menyebut "Field Fiscal Year Start atau First Accounting Period yang menyatakan penguncian" tanpa teks baris yang dimaksud; spec mengasersi tidak ada baris dengan Field tersebut selain baris yang sudah ada pada baseline (hanya satu baris Create).
  - TC-FA-PREF-602 langkah 1 merujuk "seperti TC-FA-PREF-243" untuk cara posting penyusutan pertama; spec menulis langkah fixture BE yang setara tanpa merujuk TC lain (S-04).
  - TC-FA-PREF-382 dan 602 mensyaratkan penguji mencatat baseline sebelum aksi tanpa langkah catat di bagian Langkah TC; spec menambahkannya sebagai langkah Catat (langkah 19 dan 27).
  - TC-FA-PREF-231 dan 244 memakai seri fixture PB sedangkan TC-FA-PREF-382 dan 602 memakai seri PC; spec mengasumsikan nilai awal keduanya setara (Catatan TC: seri fixture seed terisolasi).

---
id: TC-FA-PREF-E2E-091-state-tenant-suspended-dan-expired-baca-preferences-dan-changelog-tetap-tersedia-request-langsung-save-403
title: "State Tenant Suspended dan Expired: Baca Preferences dan Changelog Tetap Tersedia, Request Langsung Save Ditolak 403"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-564
  - TC-FA-PREF-565
  - TC-FA-PREF-567
  - TC-FA-PREF-568
sourceRules: ["F-FAPREF-01.k16c", "L-01a", "E-FAPREF-19", "F-FAPREF-01.k16a", "FAPREF-LOGIC-04a", "RG-02"]
smoke: []
dependsOn: []
trace:
  "F-FAPREF-01.k16c": [3, 4, 6, 7, 19, 20, 22, 23]
  "L-01a": [7, 23]
  "E-FAPREF-19": [11, 27]
  "F-FAPREF-01.k16a": [11, 13, 27, 29]
  "FAPREF-LOGIC-04a": [13, 29]
  "RG-02": [14, 15, 16, 30, 31, 32]
coverage:
  web: automated
---

# State Tenant Suspended dan Expired: Baca Preferences dan Changelog Tetap Tersedia, Request Langsung Save Ditolak 403

## Prerequisites

- Mode: FE+BE.
- Kelas harness: h (state tenant, write-lockdown Suspended dan Expired). Request langsung Save pada TC-FA-PREF-565 dan 568 mengasersi respons server dan state data, bukan perilaku FE (bagian 8b butir 1).
- Akun aktor: Total Control (Pre-setup PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup (PC-1, hanya dibaca): Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date; Changelog Preferences terisi (sedikitnya satu baris). Status entitas Suspended (PC-9) dan Expired (PC-10) dibentuk lewat fixture BE pada langkah 1 dan 17 (disediakan tim FE/BE, tanpa endpoint karangan; lihat `suite.md`, butir seed dan pemulihan lewat API).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): request langsung Save Preferences memakai sesi API Total Control Rina Anggraini (butir "Sesi API aktor" di `suite.md`) dan fixture BE untuk membaca ulang Preferences; kemampuan baca BE jumlah baris Changelog Preferences, jumlah entri System Log Rina Anggraini, dan jumlah entri Activity Log FAMS (baseline sebelum aksi, bagian 8b butir 10 dan S-12).
- State yang diubah spec: status entitas company. Langkah 33 memulihkan status ke Active; hook `after` menjalankan pemulihan yang sama dan tetap jalan bila spec gagal di tengah.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-564: Baca Preferences dan buka Changelog tetap tersedia saat entitas Suspended

1. Ubah status entitas company menjadi Suspended (PC-9) lewat fixture BE hingga tersimpan
2. Muat ulang halaman dengan F5
3. Verifikasi Tab "Preferences" menampilkan Default Capitalization Threshold "Rp 5.000.000,00"
4. Verifikasi Tab "Preferences" menampilkan nilai setting lain: Fiscal Year Start "January", First Accounting Period "March" "2026", In-service Date Source "Activation date"
5. Klik ikon View history
6. Verifikasi modal Changelog: Preferences terbuka
7. Verifikasi modal Changelog: Preferences menampilkan sedikitnya satu baris entri log
8. Klik ikon [✕] di header modal Changelog

### TC-FA-PREF-565: Request langsung Save saat entitas Suspended ditolak server dengan 403

9. Catat jumlah baris Changelog Preferences, jumlah entri System Log Rina Anggraini, dan jumlah entri Activity Log FAMS (baseline)
10. Kirim request langsung Save Preferences memakai sesi API Total Control Rina Anggraini, mengubah In-service Date Source menjadi "Manual by Accounting"
11. Verifikasi respons server 403 Forbidden
12. Baca ulang nilai Preferences tersimpan lewat fixture BE
13. Verifikasi In-service Date Source tetap "Activation date"
14. Verifikasi jumlah baris Changelog sama dengan baseline langkah 9
15. Verifikasi jumlah entri System Log Rina Anggraini sama dengan baseline langkah 9
16. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline langkah 9

### TC-FA-PREF-567: Baca Preferences dan buka Changelog tetap tersedia saat entitas Expired

17. Ubah status entitas company menjadi Expired (PC-10) lewat fixture BE hingga tersimpan
18. Muat ulang halaman dengan F5
19. Verifikasi Tab "Preferences" menampilkan Default Capitalization Threshold "Rp 5.000.000,00"
20. Verifikasi Tab "Preferences" menampilkan nilai setting lain: Fiscal Year Start "January", First Accounting Period "March" "2026", In-service Date Source "Activation date"
21. Klik ikon View history
22. Verifikasi modal Changelog: Preferences terbuka
23. Verifikasi modal Changelog: Preferences menampilkan sedikitnya satu baris entri log
24. Klik ikon [✕] di header modal Changelog

### TC-FA-PREF-568: Request langsung Save saat entitas Expired ditolak server dengan 403

25. Catat jumlah baris Changelog Preferences, jumlah entri System Log Rina Anggraini, dan jumlah entri Activity Log FAMS (baseline)
26. Kirim request langsung Save Preferences memakai sesi API Total Control Rina Anggraini, mengubah In-service Date Source menjadi "Manual by Accounting"
27. Verifikasi respons server 403 Forbidden
28. Baca ulang nilai Preferences tersimpan lewat fixture BE
29. Verifikasi In-service Date Source tetap "Activation date"
30. Verifikasi jumlah baris Changelog sama dengan baseline langkah 25
31. Verifikasi jumlah entri System Log Rina Anggraini sama dengan baseline langkah 25
32. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline langkah 25
33. Pulihkan status entitas company ke Active lewat fixture BE hingga tersimpan

## Notes

- Langkah penghubung (S-03, S-09): langkah 1 dan 17 (membentuk status entitas), langkah 2 dan 18 (muat ulang agar halaman memuat status entitas), langkah 8 dan 24 (menutup modal), dan langkah 33 (memulihkan status entitas). Layar Preferences dibuka hook `beforeEach` suite.
- Langkah 11 dan 27 mengasersi respons server saja (bagian 8b butir 1); toast atau perilaku FE untuk request langsung tidak diasersi. Jumlah baris tiga surface log diasersi sebagai selisih terhadap baseline (asersi jumlah, S-12).
- Langkah 7 dan 23 memakai "sedikitnya satu baris" sebagai asersi isi modal karena TC hanya menulis "menampilkan entri log" tanpa merinci baris dan Changelog adalah audit trail permanen (S-12, S-14).
- Temuan untuk QA:
  - TC-FA-PREF-564 dan 567 Expected b ("menampilkan entri log") tidak merinci isi baris; spec mengasersi sedikitnya satu baris.
  - TC-FA-PREF-565 dan 568 Post Condition ("Tidak ada perubahan tersimpan") dicakup oleh Expected b (In-service Date Source tetap Activation date).
  - TC-FA-PREF-565 dan 568 precondition mensyaratkan penguji mencatat baseline jumlah baris tiga surface tanpa langkah Catat di bagian Langkah TC; spec menambahkannya (langkah 9 dan 25).

---
id: TC-FA-PREF-E2E-090-state-tenant-suspended-dan-expired-save-ditolak-toast-baku-tab-tetap-dapat-dibaca
title: "State Tenant Suspended dan Expired: Save Ditolak dengan Toast Baku dan Tab Preferences Tetap Dapat Dibaca"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-227
  - TC-FA-PREF-228
  - TC-FA-PREF-563
  - TC-FA-PREF-566
sourceRules: ["F-FAPREF-01.k16c", "T-02", "F-FAPREF-01.k16b", "T-01", "F-FAPREF-01.k16a", "FAPREF-LOGIC-04a"]
smoke: []
dependsOn: []
trace:
  "F-FAPREF-01.k16c": [3, 12]
  "T-02": [6, 15, 23, 31]
  "F-FAPREF-01.k16b": [6, 15, 23, 31]
  "T-01": [8, 17]
  "F-FAPREF-01.k16a": [26, 34]
  "FAPREF-LOGIC-04a": [26, 34]
anchor: [7, 16, 24, 32]
coverage:
  web: automated
---

# State Tenant Suspended dan Expired: Save Ditolak dengan Toast Baku dan Tab Preferences Tetap Dapat Dibaca

## Prerequisites

- Mode: FE+BE.
- Kelas harness: h (state tenant, write-lockdown Suspended dan Expired).
- Akun aktor: Total Control (Pre-setup PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PB-1 untuk TC-FA-PREF-227 dan TC-FA-PREF-228 dan PC-1 untuk TC-FA-PREF-563 dan TC-FA-PREF-566 (setara: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date); akun Chart of Accounts PB-2; entitas company berstatus Active pada awal spec. Status entitas Suspended (PC-9) dan Expired (PC-10) dibentuk lewat fixture BE pada langkah 1, 10, 19, dan 27 (disediakan tim FE/BE, tanpa endpoint karangan; lihat `suite.md`, butir seed dan pemulihan lewat API).
- State yang diubah spec: status entitas company (Suspended dan Expired). Langkah 35 memulihkan status ke Active; hook `after` menjalankan pemulihan yang sama dan tetap jalan bila spec gagal di tengah. Form yang dirty dikembalikan ke nilai tersimpan pada langkah 9 dan 18; langkah 25 dan 33 memuat ulang halaman.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-227: Save ditolak saat entitas berstatus Suspended dan tab Preferences tetap dapat dibaca

1. Ubah status entitas company menjadi Suspended lewat fixture BE hingga tersimpan
2. Muat ulang halaman dengan F5
3. Verifikasi seluruh nilai setting tersimpan tampil pada tab Preferences: Fiscal Year Start "January", First Accounting Period "March" "2026", Default Capitalization Threshold "Rp 5.000.000,00", In-service Date Source "Activation date"
4. Ubah Select In-service Date Source menjadi "Manual by Accounting"
5. Klik [Save changes]
6. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tampil di kanan bawah layar
7. Verifikasi halaman tidak dialihkan
8. Verifikasi tidak ada toast sukses
9. Kembalikan Select In-service Date Source ke "Activation date"

### TC-FA-PREF-228: Save ditolak saat entitas berstatus Expired dan tab Preferences tetap dapat dibaca

10. Ubah status entitas company menjadi Expired lewat fixture BE hingga tersimpan
11. Muat ulang halaman dengan F5
12. Verifikasi seluruh nilai setting tersimpan tampil pada tab Preferences: Fiscal Year Start "January", First Accounting Period "March" "2026", Default Capitalization Threshold "Rp 5.000.000,00", In-service Date Source "Activation date"
13. Ubah Select In-service Date Source menjadi "Manual by Accounting"
14. Klik [Save changes]
15. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tampil di kanan bawah layar
16. Verifikasi halaman tidak dialihkan
17. Verifikasi tidak ada toast sukses
18. Kembalikan Select In-service Date Source ke "Activation date"

### TC-FA-PREF-563: Save saat entitas Suspended ditolak dengan toast baku

19. Ubah status entitas company menjadi Suspended (PC-9) lewat fixture BE hingga tersimpan
20. Muat ulang halaman dengan F5
21. Pilih "Manual by Accounting" pada Select In-service Date Source
22. Klik [Save changes]
23. Verifikasi toast "Changes can't be saved while this workspace is suspended or expired." tampil
24. Verifikasi halaman tidak dialihkan
25. Muat ulang tab Preferences dengan F5
26. Verifikasi In-service Date Source tetap "Activation date"

### TC-FA-PREF-566: Save saat entitas Expired ditolak dengan toast baku

27. Ubah status entitas company menjadi Expired (PC-10) lewat fixture BE hingga tersimpan
28. Muat ulang halaman dengan F5
29. Pilih "Manual by Accounting" pada Select In-service Date Source
30. Klik [Save changes]
31. Verifikasi toast "Changes can't be saved while this workspace is suspended or expired." tampil
32. Verifikasi halaman tidak dialihkan
33. Muat ulang tab Preferences dengan F5
34. Verifikasi In-service Date Source tetap "Activation date"
35. Pulihkan status entitas company ke Active lewat fixture BE hingga tersimpan

## Notes

- Langkah penghubung (S-03, S-09): langkah 1, 10, 19, dan 27 (membentuk status entitas), langkah 2, 11, 20, dan 28 (muat ulang agar halaman memuat status entitas), langkah 9 dan 18 (mengembalikan form dirty ke nilai tersimpan, tanpa Verifikasi), langkah 25 dan 33 (muat ulang Expected TC; dirty form ditangani jaring pengaman `beforeunload` hook suite), dan langkah 35 (memulihkan status entitas). Layar Preferences dibuka hook `beforeEach` suite.
- Langkah 8 dan 17 (absence toast sukses) diletakkan segera setelah pemicu dan memakai toast error pada langkah 6 dan 15 sebagai anchor positif (bagian 8b butir 2 dan 11).
- Empat blok berdiri sendiri, semuanya kelas h dengan pola seragam (parameter: status entitas dan seri fixture). TC pembacaan (TC-FA-PREF-564, 565, 567, 568) ada di spec 091.
- Temuan untuk QA:
  - TC-FA-PREF-227 dan 228 Post Condition ("Preferences company belum berubah (In-service Date Source tetap Activation date)") tidak punya langkah observasi di TC (tidak ada muat ulang) dan tidak diasersi terpisah; TC-FA-PREF-563 dan 566 mengamati nilai itu setelah muat ulang pada Expected b. Post Condition TC-FA-PREF-563 dan 566 butir "tidak ada log baru" tidak punya langkah observasi dan tidak diasersi (S-01).
  - TC-FA-PREF-227 dan 228 Expected a menyebut "Seluruh nilai setting tersimpan tampil" tanpa merinci nilai; spec mengasersi empat nilai wajib PB-1 sebagai wakil.
  - TC-FA-PREF-227 dan 228 memakai seri fixture PB sedangkan TC-FA-PREF-563 dan 566 memakai seri PC; spec mengasumsikan nilai awal keduanya setara. TC tidak menyebut cara mengubah status entitas; disediakan tim FE/BE.
  - TC-FA-PREF-563 dan 566 Expected a tidak menyebut posisi toast (kanan bawah layar) seperti TC-FA-PREF-227 dan 228; spec mengikuti teks masing-masing TC.

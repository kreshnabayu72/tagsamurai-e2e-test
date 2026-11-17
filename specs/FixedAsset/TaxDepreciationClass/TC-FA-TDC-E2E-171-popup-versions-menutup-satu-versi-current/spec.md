---
id: TC-FA-TDC-E2E-171-popup-versions-menutup-satu-versi-current
title: "Popup Versions: Menutup dan Satu Versi Current"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-611
  - TC-FA-TDC-612
sourceRules: ["§4.1.6#p5", "§4.5#b1", "§4.1.6#r10", "§4.1.6#r4", "§4.1.6#r5", "§4.1.6#r6", "§4.1.6#r7", "§4.1.6#r8"]
smoke: []
dependsOn: []
trace:
  "§4.1.6#p5": [4, 6, 7, 15]
  "§4.5#b1": 10
  "§4.1.6#r10": 14
  "§4.1.6#r4": 14
  "§4.1.6#r5": 14
  "§4.1.6#r6": 14
  "§4.1.6#r7": 14
  "§4.1.6#r8": 14
coverage:
  web: automated
---

# Popup Versions: Menutup dan Satu Versi Current

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), kunci `exampleDataBldNpVersions`: sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom sesuai Example Data kecuali BLD-NP yang memakai fixture khusus (bukan baris BLD-NP Example Data). BLD-NP memiliki 5 versi: Jan 2028 Scheduled (UL 12, SL 8.33%, Straight Line, `PMK 72/2023`, Rina P); Jan 2027 Cancelled (UL 15, SL 6.67%, Straight Line, `PMK 72/2023`, Rina P); Jan 2026 Current (UL 10, SL 10%, Straight Line, `PMK 72/2023`, Rina P); Jan 2025 Past (UL 8, SL 12.5%, Straight Line, `PMK 72/2023`, Rina P); versi pertama tanpa Effective From Past (UL 10, SL 10%, Straight Line, `UU HPP 7/2021; PMK 72/2023`, System). NB-2 memakai baris Example Data (tanpa versi lain: Useful Life 8, Straight Line Rate 12.5%, Declining Balance Rate 25%, Allowed Methods `Straight Line · Declining Balance`).
- Kemampuan teknis: membuka Drawer class dengan klik Class Code dan membuka Popup Versions dengan `View versions`; klik area gelap di luar popup (backdrop); tombol Esc.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-611: Menutup Popup Versions: ikon Close dan Esc; klik backdrop tidak menutup

1. Klik Class Code BLD-NP
2. Klik `View versions`
3. Klik area gelap di luar Popup
4. Verifikasi Popup tetap terbuka setelah klik backdrop
5. Klik ikon Close `(X)`
6. Verifikasi Popup tertutup setelah klik Close
7. Verifikasi Drawer BLD-NP tetap terbuka setelah klik Close
8. Klik `View versions` untuk membuka kembali Popup Versions
9. Tekan Esc
10. Verifikasi Popup tertutup setelah Esc
11. Tutup Drawer BLD-NP lewat `[×]`

### TC-FA-TDC-612: Class tanpa versi lain: Popup Versions memuat tepat satu versi Current

12. Klik Class Code NB-2
13. Klik `View versions`
14. Verifikasi satu baris: Effective From `—`, Status `Current`, Useful Life `8`, Straight Line Rate `12.5%`, Declining Balance Rate `25%`, Allowed Methods `Straight Line · Declining Balance`
15. Verifikasi tabel tidak pernah kosong
16. Tutup Popup Versions lewat ikon Close `(X)`
17. Tutup Drawer NB-2 lewat `[×]`

## Notes

- Urutan TC dalam spec: TC-FA-TDC-611, 612.
- Langkah penghubung (S-03): langkah 8 (membuka kembali Popup Versions dari Drawer BLD-NP yang masih terbuka; TC menulis "Buka kembali Popup Versions"), langkah 11 dan 17 (menutup Drawer tanpa perubahan lewat `[×]`; Drawer tidak dirty sehingga dialog `Unsaved Changes` tidak muncul), langkah 16 (menutup popup). Tabel utama memuat sembilan baris pada satu halaman; baris BLD-NP dan NB-2 tidak perlu dicari lewat Search (8b.13).
- Temuan untuk QA:
  - TC-FA-TDC-611 langkah 5 tidak menyebut keadaan Drawer BLD-NP setelah Esc; Expected c hanya mengasersi popup tertutup, sehingga spec menutup Drawer secara eksplisit pada langkah 11.
  - TC-FA-TDC-612 Expected b ("tabel tidak pernah kosong") bersifat kesimpulan dari butir a; spec tetap menulis `Verifikasi` sendiri (S-01).
  - Email akun Total Control dan user penyunting `Rina P` tidak tertulis di TC.

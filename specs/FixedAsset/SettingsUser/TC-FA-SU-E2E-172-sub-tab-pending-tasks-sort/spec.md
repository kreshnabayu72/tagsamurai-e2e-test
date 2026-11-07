---
id: TC-FA-SU-E2E-172-sub-tab-pending-tasks-sort
title: "Sub-tab Pending Tasks: Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-511
  - TC-FA-SU-512
  - TC-FA-SU-513
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Responsibilities (#25): pengguna target Budi Santoso dengan 5 baris Sub-tab Pending Tasks (`BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`). Nilai kolom tiap baris mengikuti Pre-setup #25; asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11).
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; perubahan tampilan (Search, Filter, Sort, Column Visibility) dipulihkan oleh langkah penghubung spec.
- Urutan default (Request Date ascending): `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`.
- Tabel parameter "Sort TC-FA-SU-511":

| Kolom | Klik 1 (ascending ↑) | Klik 2 (descending ↓) | Klik 3 (netral, default) |
|---|---|---|---|
| Transaction ID | `ASG-20260715-0045`, `ASG-20260718-0067`, `BRW-20260712-0346`, `BRW-20260713-0355`, `BRW-20260716-0372` | `BRW-20260716-0372`, `BRW-20260713-0355`, `BRW-20260712-0346`, `ASG-20260718-0067`, `ASG-20260715-0045` | `['BRW-20260712-0346', 'BRW-20260713-0355', 'ASG-20260715-0045', 'BRW-20260716-0372', 'ASG-20260718-0067']`, `['BRW-20260712-0346', 'BRW-20260713-0355', 'ASG-20260715-0045', 'BRW-20260716-0372', 'ASG-20260718-0067']` |
| Transaction | `ASG-20260715-0045`, `ASG-20260718-0067`, `BRW-20260712-0346`, `BRW-20260713-0355`, `BRW-20260716-0372` | `BRW-20260712-0346`, `BRW-20260713-0355`, `BRW-20260716-0372`, `ASG-20260715-0045`, `ASG-20260718-0067` | `['BRW-20260712-0346', 'BRW-20260713-0355', 'ASG-20260715-0045', 'BRW-20260716-0372', 'ASG-20260718-0067']`, `['BRW-20260712-0346', 'BRW-20260713-0355', 'ASG-20260715-0045', 'BRW-20260716-0372', 'ASG-20260718-0067']` |
| Status | `ASG-20260715-0045`, `ASG-20260718-0067`, `BRW-20260712-0346`, `BRW-20260713-0355`, `BRW-20260716-0372` | `BRW-20260712-0346`, `BRW-20260713-0355`, `BRW-20260716-0372`, `ASG-20260715-0045`, `ASG-20260718-0067` | `['BRW-20260712-0346', 'BRW-20260713-0355', 'ASG-20260715-0045', 'BRW-20260716-0372', 'ASG-20260718-0067']`, `['BRW-20260712-0346', 'BRW-20260713-0355', 'ASG-20260715-0045', 'BRW-20260716-0372', 'ASG-20260718-0067']` |
| Group | `ASG-20260718-0067`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260712-0346`, `BRW-20260716-0372` | `BRW-20260716-0372`, `BRW-20260712-0346`, `ASG-20260715-0045`, `BRW-20260713-0355`, `ASG-20260718-0067` | `['BRW-20260712-0346', 'BRW-20260713-0355', 'ASG-20260715-0045', 'BRW-20260716-0372', 'ASG-20260718-0067']`, `['BRW-20260712-0346', 'BRW-20260713-0355', 'ASG-20260715-0045', 'BRW-20260716-0372', 'ASG-20260718-0067']` |
- Urutan hasil sort untuk Transaction, Status, dan Group diturunkan dari data TC sumber; setiap kolom di atas dan di langkah 9 memiliki sedikitnya dua nilai distinct (S-11).

## Test Steps

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks

### TC-FA-SU-511: Sort kelas teks dan badge (Transaction ID, Transaction, Status, Group)

2. Untuk setiap baris tabel "Sort TC-FA-SU-511" (langkah 2 sampai 7): klik header kolom baris itu satu kali
3. Verifikasi urutan ascending (↑) sama dengan kolom "Klik 1" baris itu
4. Klik header kolom baris itu kedua kali
5. Verifikasi urutan descending (↓) sama dengan kolom "Klik 2" baris itu
6. Klik header kolom baris itu ketiga kali
7. Verifikasi urutan netral kembali ke default sama dengan kolom "Klik 3" baris itu

### TC-FA-SU-512: Sort kelas user (PIC)

8. Klik header PIC satu kali
9. Verifikasi urutan ascending (↑): `BRW-20260712-0346`, `BRW-20260716-0372`, `BRW-20260713-0355`, `ASG-20260718-0067`, `ASG-20260715-0045`
10. Klik header PIC kedua kali
11. Verifikasi urutan descending (↓): `ASG-20260715-0045`, `BRW-20260713-0355`, `ASG-20260718-0067`, `BRW-20260716-0372`, `BRW-20260712-0346`
12. Klik header PIC ketiga kali
13. Verifikasi urutan netral kembali ke default: `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`

### TC-FA-SU-513: Sort kelas num (Total Asset)

14. Klik header Total Asset satu kali
15. Verifikasi urutan ascending (↑): `BRW-20260713-0355`, `ASG-20260715-0045`, `ASG-20260718-0067`, `BRW-20260712-0346`, `BRW-20260716-0372`
16. Klik header Total Asset kedua kali
17. Verifikasi urutan descending (↓): `BRW-20260716-0372`, `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `ASG-20260718-0067`
18. Klik header Total Asset ketiga kali
19. Verifikasi urutan netral kembali ke default: `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): Search nama `Budi Santoso` lalu membuka Detail Budi Santoso (langkah 1). Klik ketiga tiap kolom mengembalikan sort ke netral sehingga kolom berikutnya mulai dari default (S-09).
- Langkah berulang per baris tabel parameter: tabel "Sort TC-FA-SU-511" pada langkah 2 sampai 7 (4 iterasi).
- Jumlah langkah: 19 tertulis, 37 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (37 langkah). Seluruh blok berada pada satu surface (satu sub-tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian angka di atas ambang berasal dari ekspansi iterasi tabel parameter (8b butir 7).

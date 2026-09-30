---
id: TC-GS-USER-E2E-060-responsibilities-kolom-toolbar
title: 'Kolom, urutan, dan toolbar tiap sub-tab Responsibilities'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-550
  - TC-GS-USER-551
  - TC-GS-USER-552
  - TC-GS-USER-553
  - TC-GS-USER-103
  - TC-GS-USER-546
  - TC-GS-USER-105
  - TC-GS-USER-106
  - TC-GS-USER-107
  - TC-GS-USER-381
coverage:
  web: automated
---

# Kolom, urutan, dan toolbar tiap sub-tab Responsibilities

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client dengan FAMS aktif
- User "Ahmad Fauzi" punya Borrowed `Laptop - 1` (Due `20 Aug 2026`) dan `Laptop - 2` (Due `10 Aug 2026`), Assigned `Company Vehicle B1234XY` dan `Air Conditioner - 1`, minimal tiga approval menunggu dengan Transaction dan Requester berbeda (termasuk `REQ-TRF-0089` dari "Budi Santoso", 14 Jul 2026), serta Pending Tasks campuran `Waiting for Confirmation` dan `Waiting for Acceptance` (termasuk `ASG-20260710-0004`, Group `General Affairs`, PIC "Budi Santoso")
- User "Gita Banyak" punya sedikitnya 20 baris di Borrowed Assets
- Spec ini tidak mengubah data selain preferensi kolom di browser

## Test Steps

### Borrowed Assets

1. Buka User Detail "Ahmad Fauzi" > Tab Responsibilities > sub-tab Borrowed Assets
2. Verifikasi 8 kolom: Photo, Transaction ID (format `BRW-YYYYMMDD-XXXX`), Name (mis. `Laptop - 1`), Asset ID, Brand, Model / Type, Due Return Date, PIC, dan `Laptop - 2` berada di atas `Laptop - 1` (Due Return Date naik)
3. Cari kata kunci dari tiap kolom yang bisa dicari (Transaction ID, Name, Asset ID, Brand, Model / Type, PIC) lalu cari tanggal Due Return Date
4. Verifikasi kolom teks menemukan baris terkait, sedangkan Photo dan Due Return Date tidak dapat dicari
5. Buka Filter dan verifikasi field Name, Brand, Due Return Date, PIC, lalu Download dan verifikasi nama berkas `Borrowed-Assets-Ahmad-Fauzi`

### Assigned Assets

6. Buka sub-tab Assigned Assets
7. Verifikasi 7 kolom: Photo, Transaction ID (`ASG-...`), Name, Asset ID, Brand, Model / Type, PIC, tanpa Due Return Date atau Assigned Date, dan `Air Conditioner - 1` di atas (Name A-Z)
8. Verifikasi Filter berisi Name, Brand, PIC dan Download menghasilkan berkas `Assigned-Assets-Ahmad-Fauzi`

### Pending Approvals

9. Buka sub-tab Pending Approvals
10. Verifikasi 4 kolom: Transaction ID (teks biasa, bukan tautan) `REQ-TRF-0089`, Transaction `Transfer`, Requester "Budi Santoso", Submission Date `14 Jul 2026`, tanpa kolom `subject`, Status, Group, atau PIC, dan urutan default Submission Date terlama dulu
11. Cari `REQ-TRF`, nama Requester, dan `Transfer`, lalu verifikasi pencarian cocok untuk Transaction ID dan Requester tetapi tidak untuk kolom Transaction dan Submission Date
12. Filter Transaction dengan minimal dua nilai lalu Apply, kemudian filter Requester dan Submission Date, dan verifikasi Transaction memakai OR antar nilai
13. Download dan verifikasi nama berkas `Pending-Approvals-Ahmad-Fauzi`

### Pending Tasks

14. Buka sub-tab Pending Tasks
15. Verifikasi 8 kolom: Transaction ID (teks biasa), Transaction (`Borrowing` atau `Assignment`), Status (badge `Waiting for Confirmation` untuk Borrowing dan `Waiting for Acceptance` untuk Assignment), Group, PIC, Total Asset, Request Date, Last Updated, dengan urutan default Request Date terlama dulu
16. Cari `ASG-`, `General`, `Budi`, `Assignment` dan verifikasi pencarian cocok untuk Transaction ID, Group, PIC tetapi tidak untuk Transaction, Status, dan tanggal
17. Terapkan keenam filter (Transaction multi-select, Status, Group, PIC, Request Date, Last Updated) dan verifikasi semuanya berfungsi, lalu Download dan verifikasi nama berkas `Pending-Tasks-Ahmad-Fauzi`
18. Klik header kolom Status satu, dua, dan tiga kali
19. Verifikasi klik pertama mengurutkan A-Z menurut label badge, klik kedua Z-A, dan klik ketiga menghapus indikator dan kembali ke urutan default Request Date terlama dulu

### Tanpa navigasi

20. Klik satu baris di sub-tab Borrowed Assets, Assigned Assets, Pending Approvals, dan Pending Tasks
21. Verifikasi tidak ada navigasi atau deep-link keluar pada keempatnya (display-only)

### Pencarian di sisi klien dan Pin kolom

22. Buka User Detail "Gita Banyak" > Tab Responsibilities > Borrowed Assets, lalu ketik kata kunci di Search
23. Verifikasi hasil terfilter tanpa permintaan jaringan baru ke server
24. Buka Column Visibility (ikon Actions), Pin kolom `Name`, lalu scroll tabel ke samping pada viewport sempit
25. Verifikasi kolom `Name` tetap di posisinya saat scroll, Hide dan Drag Reorder berfungsi untuk semua kolom, dan tidak bisa menyembunyikan kolom terakhir yang visible

## Notes

- Sumber `user.md` bagian 4.1, 4.2a, 4.2b, dan 4.4, serta `prd-conventions.md` bagian 9.3 dan 9.7.
- Detail kolom Pending Approvals versi Admin Console sama dan dicakup di `TC-GS-USER-E2E-059-responsibilities-gating-subscription`.
- Spec ini menggabungkan banyak layar karena semuanya satu topik: tabel display-only Tab Responsibilities. Bila terlalu panjang saat dieksekusi, pecah per sub-tab.

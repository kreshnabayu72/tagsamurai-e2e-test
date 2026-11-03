---
id: TC-FA-RP-E2E-009-sidebar-group-tree-elemen-state-pencarian-dan-empty-state-1
title: "Sidebar Group Tree: elemen, state, pencarian, dan empty state (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-29
  - TC-FA-RP-30
  - TC-FA-RP-31
coverage:
  web: automated
---

# Sidebar Group Tree: elemen, state, pencarian, dan empty state (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #18 (pohon group `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`, `Helpdesk`, `Logistics Warehouse` > `Dock 1`), #43 (seed Group Manager: Fajar Nugroho di `IT Infrastructure`, Kevin Susanto di `Data Center`, Lina Marlina di `Head Office`).
- State UI yang diubah: panel Sidebar Group Tree ditutup dan dibuka kembali pada TC-FA-RP-30; state tersimpan per user per halaman. Spec berakhir dengan panel terbuka sehingga tidak ada pemulihan tambahan.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun dan nama group ditambahkan tim FE.
- Kemampuan teknis: hover untuk membaca tooltip. Spec tidak mengubah data dan tidak mengubah state global.

## Test Steps

### TC-FA-RP-29: Screening Sidebar Group Tree di Tab Group Manager

1. Klik Tab `Group Manager`
2. Verifikasi header panel berjudul `Groups` rata kiri
3. Verifikasi satu baris berisi kolom pencarian tree dengan placeholder `Search group name...` dan tombol Expand/Collapse All
4. Verifikasi node `All Groups` aktif dan ter-highlight
5. Klik tombol Expand/Collapse All
6. Verifikasi pohon `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`, `Helpdesk`, `Logistics Warehouse` > `Dock 1` terbuka
7. Verifikasi tidak ada tombol aksi `Group`, tidak ada menu `⋯` per node, tidak ada indikator function, dan tidak ada badge jumlah per node
8. Arahkan kursor ke floating toggle di tepi panel
9. Verifikasi tooltip floating toggle `Collapse Group Tree` saat panel terbuka

### TC-FA-RP-30: Collapse, buka kembali, dan state tersimpan per user per halaman

10. Klik floating toggle `Collapse Group Tree`
11. Verifikasi panel menutup
12. Verifikasi tabel melebar penuh
13. Verifikasi toggle berpindah ke tepi kanan layar
14. Arahkan kursor ke toggle di tepi kanan layar
15. Verifikasi tooltip toggle `Open Group Tree`
16. Muat ulang halaman (F5)
17. Verifikasi setelah F5 panel tetap tertutup
18. Klik toggle `Open Group Tree`
19. Verifikasi panel terbuka kembali
20. Arahkan kursor ke toggle
21. Verifikasi tooltip toggle kembali `Collapse Group Tree`

### TC-FA-RP-31: Seleksi tunggal, filter literal tanpa pewarisan, All Groups gabungan

22. Klik node `IT Infrastructure`
23. Verifikasi hanya baris penugasan langsung pada `IT Infrastructure` (Fajar Nugroho) tampil
24. Verifikasi baris `Data Center` tidak ikut tampil walau descendant
25. Klik node `Data Center`
26. Verifikasi hanya baris Kevin Susanto di `Data Center` tampil
27. Verifikasi node `Data Center` ter-highlight dan hanya satu node aktif
28. Klik node `Rack A1`
29. Verifikasi tabel menampilkan empty state `No group managers yet`
30. Klik node `Rack A1` yang sedang aktif sekali lagi
31. Verifikasi klik node aktif tidak men-toggle dan tidak mengubah tampilan (empty state `No group managers yet` tetap tampil)
32. Klik node `All Groups`
33. Verifikasi gabungan seluruh baris dalam cakupan aktor tampil kembali (Fajar Nugroho, Kevin Susanto, dan Lina Marlina)

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-29, 30, 31). TC-FA-RP-32, 33, 34 ada di spec `TC-FA-RP-E2E-010-sidebar-group-tree-elemen-state-pencarian-dan-empty-state-2`.
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab, klik tombol Expand/Collapse All untuk membuka pohon (TC-FA-RP-29 menyatakan pohon "dapat dibuka") dan hover toggle.
- Temuan untuk QA:
  - TC-FA-RP-31 expected a menyebut baris `IT Infrastructure` hanya Fajar Nugroho; Pre-setup #43 hanya menyebut tiga penugasan Group Manager sehingga Kevin Susanto di `Helpdesk` (Pre-setup #38) tidak dipakai.
  - TC-FA-RP-29 menulis "pohon dapat dibuka" tanpa langkah untuk membukanya; spec memakai tombol Expand/Collapse All.
  - Post Condition TC-FA-RP-29, 30, dan 31 tidak memberi langkah observasi tambahan; tidak diasersi.

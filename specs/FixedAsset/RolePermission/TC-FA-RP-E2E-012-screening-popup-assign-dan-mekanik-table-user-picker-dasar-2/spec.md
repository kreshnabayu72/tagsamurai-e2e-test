---
id: TC-FA-RP-E2E-012-screening-popup-assign-dan-mekanik-table-user-picker-dasar-2
title: "Screening popup Assign dan mekanik Table User Picker dasar (2/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-39
  - TC-FA-RP-40
  - TC-FA-RP-41
  - TC-FA-RP-42
coverage:
  web: automated
---

# Screening popup Assign dan mekanik Table User Picker dasar (2/3)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #15 (pool pengguna sebagai kandidat), #17 (variasi Home Group), #18 (pohon group `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`, `Helpdesk`), #19 (seed Role Transaksi pada `IT Infrastructure` sub-tab Disposal). Spec hanya membaca dan membatalkan popup; tidak mengubah data.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama group, dan nama pengguna ditambahkan tim FE.
- Kemampuan teknis: tidak ada tambahan. Spec tidak mengubah state global.

## Test Steps

### TC-FA-RP-39: Screening popup Assign User, Group Role (field Group default dari Sidebar)

1. Klik Tab `System`, buka Detail Role `Manage files`, lalu klik node `Data Center` di Sidebar Group Tree
2. Klik `[+ Assign]`
3. Verifikasi Modal berjudul `Assign User — Manage files (Data Center)` mengikuti nilai field Group
4. Verifikasi field Group terisi `Data Center` dari node aktif Sidebar
5. Verifikasi preview scope menampilkan `Data Center` dan `Rack A1`
6. Pilih group `Helpdesk` pada field Group
7. Verifikasi popup tetap terbuka dan field Group berisi `Helpdesk` (nilai dapat diubah manual tanpa menutup popup)
8. Pilih group `Data Center` pada field Group
9. Klik `[✕]` untuk menutup popup

### TC-FA-RP-40: Screening popup Assign Asset Admin pada Tab Transaction Role

10. Klik Tab `Transaction Role`, klik node `IT Infrastructure`, lalu klik sub-tab `Disposal`
11. Klik `[+ Assign]` pada section Asset Admin
12. Verifikasi Modal berjudul `Assign Asset Admin (IT Infrastructure)` (pola `Assign [Role Name] ([Group Name])`)
13. Verifikasi struktur toolbar, kolom, dan footer popup Assign sama dengan popup Assign lain
14. Verifikasi tidak ada field Group (group mengikuti node terpilih)
15. Verifikasi sedikitnya satu baris kandidat tampil
16. Verifikasi aktor sendiri tidak ada di daftar
17. Klik `[✕]` untuk menutup popup

### TC-FA-RP-41: Screening popup Assign Monitoring & Report pada Tab Transaction Role

18. Klik `[+ Assign]` pada section Monitoring & Report
19. Verifikasi Modal berjudul `Assign Monitoring & Report (IT Infrastructure)`
20. Verifikasi struktur toolbar, kolom, dan footer popup Assign sama dengan popup Assign lain
21. Verifikasi tidak ada field Group (group mengikuti node terpilih)
22. Verifikasi sedikitnya satu baris kandidat tampil
23. Verifikasi aktor sendiri tidak ada di daftar
24. Klik `[✕]` untuk menutup popup

### TC-FA-RP-42: Screening popup Assign Staff pada Tab Transaction Role

25. Klik `[+ Assign]` pada section Staff
26. Verifikasi Modal berjudul `Assign Staff (IT Infrastructure)`
27. Verifikasi struktur toolbar, kolom, dan footer popup Assign sama dengan popup Assign lain
28. Verifikasi tidak ada field Group (group mengikuti node terpilih)
29. Verifikasi sedikitnya satu baris kandidat tampil
30. Verifikasi aktor sendiri tidak ada di daftar
31. Klik `[✕]` untuk menutup popup

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-39, 40, 41, 42). TC-FA-RP-35 sampai 38 ada di spec `TC-FA-RP-E2E-011-screening-popup-assign-dan-mekanik-table-user-picker-dasar-1`; TC-FA-RP-43 (Assign Approver) ada di spec `TC-FA-RP-E2E-013-screening-popup-assign-dan-mekanik-table-user-picker-dasar-3`.
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab, node, dan sub-tab; membuka Detail Role; mengganti lalu mengembalikan nilai field Group sebelum menutup popup TC-FA-RP-39; dan menutup popup dengan `[✕]`.
- Absence daftar kandidat (aktor sendiri) didahului `Verifikasi` sedikitnya satu baris kandidat tampil pada popup yang sama (8b butir 2).
- Pola header PRD (`Assign User — [Role Name] ([Group Name])` dan `Assign [Role Name] ([Group Name])`) dicakup oleh `Verifikasi` judul modal.
- Temuan untuk QA:
  - TC-FA-RP-39 expected b menyatakan nilai Group "dapat diubah manual" tanpa menyebut group tujuan atau perilaku saat popup ditutup setelah nilai diubah; spec memilih `Helpdesk` lalu mengembalikan `Data Center` sebelum menutup, tanpa mengasersi dialog `Unsaved Changes`.
  - Post Condition TC-FA-RP-39, 40, 41, dan 42 tidak memberi langkah observasi tambahan; tidak diasersi.

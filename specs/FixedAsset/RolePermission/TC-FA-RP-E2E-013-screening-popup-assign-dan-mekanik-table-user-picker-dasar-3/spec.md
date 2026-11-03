---
id: TC-FA-RP-E2E-013-screening-popup-assign-dan-mekanik-table-user-picker-dasar-3
title: "Screening popup Assign dan mekanik Table User Picker dasar (3/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-43
  - TC-FA-RP-44
  - TC-FA-RP-45
coverage:
  web: automated
---

# Screening popup Assign dan mekanik Table User Picker dasar (3/3)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #15 (pool pengguna sebagai kandidat popup Assign), #17 (variasi Home Group), #18 (pohon group), #19 (seed Role Transaksi pada `IT Infrastructure` sub-tab Disposal). Spec hanya membaca, memilih baris pada popup, dan membatalkan popup; tidak mengubah data.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun dan nama group ditambahkan tim FE.
- Kemampuan teknis: tidak ada tambahan. Spec tidak mengubah state global.

## Test Steps

### TC-FA-RP-43: Screening popup Assign Approver pada Tab Transaction Role

1. Klik Tab `Transaction Role`, klik node `IT Infrastructure`, lalu klik sub-tab `Disposal`
2. Klik `[+ Assign]` pada section Approver
3. Verifikasi Modal berjudul `Assign Approver (IT Infrastructure)` (pola `Assign [Role Name] ([Group Name])`)
4. Verifikasi struktur toolbar, kolom, dan footer popup Assign sama dengan popup Assign lain
5. Verifikasi tidak ada field Group (group mengikuti node terpilih)
6. Verifikasi sedikitnya satu baris kandidat tampil
7. Verifikasi aktor sendiri tidak ada di daftar
8. Klik `[✕]` untuk menutup popup

### TC-FA-RP-44: Table User Picker, Selection Mode, counter, dan penutupan popup tanpa dialog

9. Klik Tab `Total Control`, lalu klik `[+ Assign]`
10. Centang satu baris
11. Verifikasi Bulk Action Bar tanpa menu aksi menampilkan `1 User selected`
12. Centang baris kedua
13. Verifikasi counter `2 Users selected`
14. Centang checkbox header Select All
15. Verifikasi seluruh baris pada halaman aktif tercentang
16. Verifikasi counter `[N] Users selected` dengan N sama dengan jumlah baris halaman aktif
17. Klik `[✕]`
18. Verifikasi popup tertutup tanpa dialog `Unsaved Changes`
19. Verifikasi tidak ada toast
20. Klik `[+ Assign]`
21. Verifikasi seleksi dibuang: counter bar tidak tampil
22. Klik `[✕]` untuk menutup popup

### TC-FA-RP-45: Klik `[Assign]` tanpa seleksi menampilkan alert inline

23. Klik `[+ Assign]` di Tab `Total Control`
24. Klik `[Assign]` tanpa memilih user
25. Verifikasi alert inline rata kanan di atas footer dengan severity danger: `You must pick a user`
26. Verifikasi popup tetap terbuka
27. Verifikasi tidak ada toast
28. Klik `[✕]` untuk menutup popup

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-43, 44, 45). TC-FA-RP-35 sampai 42 ada di spec `TC-FA-RP-E2E-011-screening-popup-assign-dan-mekanik-table-user-picker-dasar-1` dan `TC-FA-RP-E2E-012-screening-popup-assign-dan-mekanik-table-user-picker-dasar-2`.
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab, node, dan sub-tab; membuka ulang popup `[+ Assign]` sesudah TC-FA-RP-44 untuk mengamati bahwa seleksi dibuang; menutup popup dengan `[✕]`.
- Absence daftar kandidat (aktor sendiri) didahului `Verifikasi` sedikitnya satu baris kandidat tampil pada popup yang sama (8b butir 2). Absence toast pada TC-FA-RP-44 dan TC-FA-RP-45 diletakkan segera setelah pemicunya (8b butir 11).
- Temuan untuk QA:
  - TC-FA-RP-44 expected d menyatakan "seleksi dibuang" tanpa langkah untuk mengamatinya; spec membuka ulang popup dan memverifikasi counter bar tidak tampil.
  - TC-FA-RP-45 expected b menyebut "tidak ada permintaan tersimpan" tanpa langkah observasi; spec hanya memverifikasi popup tetap terbuka dan tidak ada toast.
  - Post Condition TC-FA-RP-43, 44, dan 45 tidak memberi langkah observasi tambahan; tidak diasersi.

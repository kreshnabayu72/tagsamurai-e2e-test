---
id: TC-FA-ASTL-BE-093-state-tenant-server
title: "Server menolak tulis saat entitas Suspended atau Expired"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [ASTL-LOGIC-01d, EB-AKS-7]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-01d: [5, 7, 9, 11, 13, 15, 17, 20, 22, 24, 27, 29, 31, 33]
  EB-AKS-7: [3, 5, 7, 9, 11, 13, 20, 22, 27, 29, 33]
anchor: []
---

# Server menolak tulis saat entitas Suspended atau Expired

## Prerequisites
- Aktor: Total Control (Hendra).
- Data:
  - DU-093-1: Entitas, entitas khusus berstatus Active pada awal dan tidak dipakai spec lain: Name `Entitas Uji Status {runId}`, Status awal `Active`.
  - DU-093-2: User, total Control seluruh entitas: Name `Hendra Saputra {runId}`, Role `Total Control`, Cakupan `Seluruh entitas`.
  - DU-093-3: Group, group dengan Available license satu: Name `Kantor Uji {runId}`, Available license `1`.
  - DU-093-4: Asset, aset dengan Purchase Cost 18,5 juta: Name `Laptop Pro 16 - A1 {runId}`, Lifecycle `Active`, Group `Kantor Uji {runId}`, Purchase Cost `18500000.00`.
  - DU-093-5: Asset, aset berlabel manual: Name `Laptop Pro 16 - A2 {runId}`, Lifecycle `Active`, Group `Kantor Uji {runId}`, Label manual `Inventaris Kantor {runId}`.
  - DU-093-6: Asset, aset Unmanaged untuk Manage: Name `Tablet Inventaris - A3 {runId}`, Lifecycle `Active`, Group `Kantor Uji {runId}`, Status `Unmanaged`.
  - DU-093-7: Asset, aset Unmanaged yang dapat dihapus: Name `Kursi Kerja - A4 {runId}`, Lifecycle `Active`, Group `Kantor Uji {runId}`, Status `Unmanaged`, Custody `Available`, Jejak finansial `tidak ada`.
  - DU-093-8: Asset, aset Pending Activation yang aktivasinya berhasil: Name `Tablet Inventaris - P1 {runId}`, Lifecycle `Active`, Group `Kantor Uji {runId}`, Status `Pending Activation`.
  - DU-093-9: Asset, aset Pending Activation yang aktivasinya gagal: Name `Tablet Inventaris - P2 {runId}`, Lifecycle `Active`, Group `Kantor Uji {runId}`, Status `Pending Activation`.
  - DU-093-10: Asset, aset Pending Activation yang aktivasinya berhasil: Name `Tablet Inventaris - P3 {runId}`, Lifecycle `Active`, Group `Kantor Uji {runId}`, Status `Pending Activation`.
  - DU-093-11: Asset, aset Pending Activation yang aktivasinya gagal: Name `Tablet Inventaris - P4 {runId}`, Lifecycle `Active`, Group `Kantor Uji {runId}`, Status `Pending Activation`.
  - DU-093-14: Asset, aset Unmanaged untuk Manage lewat Switch: Name `Tablet Inventaris - A6 {runId}`, Lifecycle `Active`, Group `Kantor Uji {runId}`, Status `Unmanaged`.
  - DU-093-15: Asset, aset managed yang menjadi pasangan Switch: Name `Printer Laser - A5 {runId}`, Lifecycle `Active`, Group `Kantor Uji {runId}`, Status `Managed`.
- Kondisi: aktivasi `Tablet Inventaris - P2 {runId}` dan `Tablet Inventaris - P4 {runId}` gagal ketika Managed Transition Time berakhir.

## Test Steps

### Entitas Suspended menolak seluruh aksi tulis namun tetap terbaca
1. Entitas `Entitas Uji Status {runId}` berstatus Suspended
2. Hendra meminta daftar aset
3. Verifikasi daftar aset terbaca dan memuat `Laptop Pro 16 - A1 {runId}` tanpa gerbang akses
4. Hendra menambahkan label `Prioritas {runId}` pada `Laptop Pro 16 - A1 {runId}`
5. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.` dan `Laptop Pro 16 - A1 {runId}` tidak berlabel `Prioritas {runId}`
6. Hendra mencabut label `Inventaris Kantor {runId}` dari `Laptop Pro 16 - A2 {runId}`
7. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.` dan `Laptop Pro 16 - A2 {runId}` tetap berlabel `Inventaris Kantor {runId}`
8. Hendra meng-Manage aset `Tablet Inventaris - A3 {runId}` dengan sumber `Available quota`
9. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.` dan `Tablet Inventaris - A3 {runId}` tetap `Unmanaged`
10. Hendra menjalankan Delete Asset Data pada aset `Kursi Kerja - A4 {runId}`
11. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.` dan `Kursi Kerja - A4 {runId}` tetap ada
12. Hendra menyimpan Edit Purchase pada `Laptop Pro 16 - A1 {runId}` dengan Purchase Cost `20000000.00`
13. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.` dan Purchase Cost `Laptop Pro 16 - A1 {runId}` tetap `18500000.00`

### Job aktivasi System tetap berjalan pada entitas Suspended
14. Aktivasi `Tablet Inventaris - P1 {runId}` berhasil ketika Managed Transition Time berakhir
15. Verifikasi `Tablet Inventaris - P1 {runId}` menjadi managed dan Changelog-nya memuat entri `Pending Activation` ke `Managed` dengan pelaku `System`
16. Aktivasi `Tablet Inventaris - P2 {runId}` gagal ketika Managed Transition Time berakhir
17. Verifikasi `Tablet Inventaris - P2 {runId}` kembali `Unmanaged` dan Changelog-nya memuat entri `Pending Activation` ke `Unmanaged` dengan pelaku `System`

### Entitas Expired menolak aksi tulis dan job System tetap berjalan
18. Entitas `Entitas Uji Status {runId}` berstatus Expired
19. Hendra menyimpan Edit Purchase pada `Laptop Pro 16 - A1 {runId}` dengan Purchase Cost `20000000.00`
20. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.` dan Purchase Cost `Laptop Pro 16 - A1 {runId}` tetap `18500000.00`
21. Hendra menambahkan label `Prioritas {runId}` pada `Laptop Pro 16 - A1 {runId}`
22. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.` dan `Laptop Pro 16 - A1 {runId}` tidak berlabel `Prioritas {runId}`
23. Aktivasi `Tablet Inventaris - P3 {runId}` berhasil ketika Managed Transition Time berakhir
24. Verifikasi `Tablet Inventaris - P3 {runId}` menjadi managed dan Changelog-nya memuat entri `Pending Activation` ke `Managed` dengan pelaku `System`

### Entitas pada masa Grace menolak aksi tulis dan job System tetap berjalan
25. Entitas `Entitas Uji Status {runId}` berstatus Grace
26. Hendra menjalankan Delete Asset Data pada aset `Kursi Kerja - A4 {runId}`
27. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.` dan `Kursi Kerja - A4 {runId}` tetap ada
28. Hendra meng-Manage aset `Tablet Inventaris - A3 {runId}` dengan sumber `Available quota`
29. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.` dan `Tablet Inventaris - A3 {runId}` tetap `Unmanaged`
30. Aktivasi `Tablet Inventaris - P4 {runId}` gagal ketika Managed Transition Time berakhir
31. Verifikasi `Tablet Inventaris - P4 {runId}` kembali `Unmanaged` dan Changelog-nya memuat entri `Pending Activation` ke `Unmanaged` dengan pelaku `System`

### Manage dengan sumber Switch ditolak pada entitas Grace
32. Hendra meng-Manage aset `Tablet Inventaris - A6 {runId}` dengan sumber Switch, menukar aset managed `Printer Laser - A5 {runId}`
33. Verifikasi permintaan ditolak dengan pesan `Changes can't be saved while this workspace is suspended or expired.`, `Tablet Inventaris - A6 {runId}` tetap `Unmanaged`, dan `Printer Laser - A5 {runId}` tetap managed

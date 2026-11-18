---
id: TC-FA-ASTL-E2E-034-pencabutan-hak-saat-halaman-terbuka
title: "Hak dicabut saat halaman terbuka"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-14f", "ASTL-LOGIC-20k", "ASTL-LOGIC-20l", "ASTL-LOGIC-20m", "T-21", "EC-44", "EB-AKS-6"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-14f": [2, 4, 6, 7]
  "ASTL-LOGIC-20k": 17
  "ASTL-LOGIC-20l": 18
  "ASTL-LOGIC-20m": [10, 19]
  "T-21": 17
  "EC-44": [10, 18, 19]
  "EB-AKS-6": [17, 20]
anchor: []
coverage:
  web: automated
---

# Hak dicabut saat halaman terbuka

## Prerequisites
- Aktor: `Sari Wulandari {runId}`, pemegang role Manage asset & TAG (Read + Update) dan Manage purchase (Read) pada group `IT {runId}` beserta descendant.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-034-1: User, Name `Sari Wulandari {runId}`, Role `Manage asset & TAG dan Manage purchase`, Cakupan `Group IT {runId} beserta descendant`
  - DU-034-2: Group, Name `IT {runId}`
  - DU-034-3: Group, Name `GA {runId}`
  - DU-034-4: Asset, Name `Laptop Pro 16 {runId}`, Group `IT {runId}`, Status `Available`, Purchase Date `T0 − 30 hari`, Purchase Cost `18500000`
  - DU-034-5: Asset, Name `Printer Laser {runId}`, Group `GA {runId}`, Status `Available`, Purchase Date `T0 − 30 hari`, Purchase Cost `7250000`
  - DU-034-6: Label, Name `Aset Kantor {runId}`
  - Nama baris yang diharapkan untuk Asset Name `Laptop Pro 16 {runId}` adalah `Laptop Pro 16 {runId} - 1`, dari Asset Name `Laptop Pro 16 {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Printer Laser {runId}` adalah `Printer Laser {runId} - 1`, dari Asset Name `Printer Laser {runId}`.
  - Purchase Cost yang diharapkan untuk Purchase Cost `7250000` adalah `Rp 7.250.000,00`, dari Purchase Cost `7250000`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Lisensi `FA-7` aktif pada entitas.

## Test Steps

### Node group keluar dari cakupan mengembalikan pilihan ke All Groups
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Laptop Pro 16 {runId} - 1` tampil di tabel
3. Klik node `IT {runId}` pada Sidebar Group
4. Verifikasi node `IT {runId}` menjadi node aktif Sidebar Group
5. Admin memindahkan penugasan `Sari Wulandari {runId}` dari group `IT {runId}` ke group `GA {runId}`
6. Verifikasi node aktif Sidebar Group kembali ke `All Groups`
7. Verifikasi Sidebar Group memuat node `GA {runId}` dan tidak memuat node `IT {runId}`

### Hak dicabut saat halaman terbuka
8. Ketik Search `{runId}`, tekan Enter
9. Tampilkan kolom `Purchase Cost`
10. Verifikasi sel `Purchase Cost` baris `Printer Laser {runId} - 1` menampilkan `Rp 7.250.000,00`
11. Admin mencabut hak `Manage purchase` dan hak Update `Manage asset & TAG` dari `Sari Wulandari {runId}` pada group `GA {runId}`
12. Centang baris `Printer Laser {runId} - 1`
13. Klik tombol Bulk Action
14. Klik `Add Label`
15. Pilih label `Aset Kantor {runId}` pada dialog Add Label
16. Klik `[Apply]`
17. Verifikasi toast `You don't have permission to do this.` tampil
18. Verifikasi tabel dimuat ulang otomatis tanpa aksi pengguna
19. Verifikasi sel `Purchase Cost` baris `Printer Laser {runId} - 1` menampilkan `No access`
20. Verifikasi checkbox baris dan Bar Bulk tidak dirender (Hidden) bagi aktor

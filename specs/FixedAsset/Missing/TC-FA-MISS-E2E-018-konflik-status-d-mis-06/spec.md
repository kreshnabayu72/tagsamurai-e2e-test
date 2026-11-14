---
id: TC-FA-MISS-E2E-018-konflik-status-d-mis-06
title: "Konflik status: aksi atas record yang sudah diubah admin lain menampilkan Already Changed dan Reload"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§6#r10", "§7.2#r9", "§7.2#r13", "§4.2.4#p13", "§4.2.4#r23", "§4.4#r13", "§9.2#b20", "§9.4.2#r28", "§9.6#p2", "§9.4.4#r7", "EB-ERR-4", "EB-CON-3"]
smoke: []
dependsOn: []
trace:
  "§6#r10": 7
  "§7.2#r9": [7, 8]
  "§7.2#r13": 7
  "§4.2.4#p13": 7
  "§4.2.4#r23": 11
  "§4.4#r13": [7, 11]
  "§9.2#b20": [7, 16]
  "§9.4.2#r28": [7, 16]
  "§9.6#p2": 7
  "§9.4.4#r7": [7, 11, 16]
  "EB-ERR-4": 16
  "EB-CON-3": 7
anchor: [10, 15]
coverage:
  web: automated
---

# Konflik status: aksi atas record yang sudah diubah admin lain menampilkan Already Changed dan Reload

## Prerequisites
- Aktor: Rina W, Total Control, tidak menjadi Last Holder record di bawah; Andi P, Group Manager pada Group Head Office, yang memicu perubahan status record (LK-8).
- Layar awal: halaman Missing, sub-tab Active.
- Data:
  - DU-018-1: Record Missing `Welder Machine Lincoln {runId}`, Asset ID `WLD-018-0001`, Group `Finance Room`, Status `Missing`, Source `Manual`, Last Holder `—`, Reported By `Rina W`, Reported Date `T0 − 4 hari, pukul 09:30`.
  - DU-018-2: Record Missing `Air Compressor Puma {runId}`, Asset ID `CMP-018-0002`, Group `Finance Room`, Status `Missing`, Source `Manual`, Last Holder `—`, Reported By `Rina W`, Reported Date `T0 − 5 hari, pukul 09:45`; tidak diubah spec ini.
  - DU-018-3: Isian Add Update yang ditolak karena status record sudah berubah: Update `Pemeriksaan bengkel selesai, mesin las tidak ditemukan di lokasi servis`.
  - DU-018-4: Isian Mark as Found oleh Andi P atas DU-018-1: Found at `Finance Room`, Asset Status `Normal`. Node yang diharapkan: `Marked as found by Andi P`.
  - Pengguna pada data: Rina W, Total Control, seluruh client; Andi P, Group Manager pada Group Head Office beserta sub-group.
  - Waktu pada data ditulis relatif terhadap waktu run `T0`.

## Test Steps

### Add Update ditolak karena status record sudah diubah admin lain
1. Ketik Search `{runId}`, tekan Enter
2. Klik `⋯` pada baris `Welder Machine Lincoln {runId}`
3. Klik `Add Update`
4. Isi Update `Pemeriksaan bengkel selesai, mesin las tidak ditemukan di lokasi servis`
5. Andi P menjalankan Mark as Found atas record `Welder Machine Lincoln {runId}` dengan Found at `Finance Room` dan Asset Status `Normal`
6. Klik `[Add Update]`
7. Verifikasi dialog `Already Changed` tampil dengan pesan `This record was changed by [User Name]. Reload to see the latest status.` untuk User Name `Andi P`
8. Verifikasi tombol `[Reload]` tampil pada dialog `Already Changed`
### Reload memuat ulang tabel dan record tidak menerima Update
9. Klik `[Reload]`
10. Verifikasi baris `Air Compressor Puma {runId}` tetap tampil di sub-tab Active
11. Verifikasi baris `Welder Machine Lincoln {runId}` tidak tampil lagi di sub-tab Active setelah daftar dimuat ulang
12. Klik sub-tab `History`
13. Ketik Search `{runId}`, tekan Enter
14. Klik nama `Welder Machine Lincoln {runId}` pada kolom Name
15. Verifikasi node `Marked as found by Andi P` tampil pada record
16. Verifikasi node `Update added by Rina W` tidak ada pada record karena Add Update ditolak tanpa efek ganda

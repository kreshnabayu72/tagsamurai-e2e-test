---
id: TC-FA-FAREG-E2E-065-kunci-sesi-view-only-delete-terkunci
title: "Kunci sesi: View only dan Delete batch yang terkunci"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [F-FAREG-03.k2, FAREG-LOGIC-19b, FAREG-LOGIC-19f, FAREG-LOGIC-20b, §4.8#r16, §4.8#r26, §9.4.2#r25, §9.4.2#r26, D-REG-22, D-REG-27, S-REG-26]
smoke: [D-REG-22, D-REG-27, S-REG-26]
dependsOn: []
trace:
  F-FAREG-03.k2: [3, 17]
  FAREG-LOGIC-19b: [5, 7]
  FAREG-LOGIC-19f: [17, 21]
  FAREG-LOGIC-20b: [7, 14]
  §4.8#r16: 3
  §4.8#r26: [3, 5]
  §9.4.2#r25: [17, 21]
  §9.4.2#r26: [3, 7]
  D-REG-22: [4, 5, 14]
  D-REG-27: [18, 19]
  S-REG-26: [7, 8, 9]
anchor: [12]
coverage:
  web: automated
---

# Kunci sesi: View only dan Delete batch yang terkunci

## Prerequisites
- Aktor: `Hadi K` (Manage asset & TAG, Group terkelola `Gudang Terkunci {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - DU-065-1: Draft tersimpan milik `Rina W` untuk Group `Gudang Terkunci {runId}`. Item 1 `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `2`.
- Kondisi:
  - Kunci sesi batch `Gudang Terkunci {runId}` dipegang `Rina W` (Manage asset & TAG, Group terkelola `Gudang Terkunci {runId}`), yang sedang membuka form Edit batch itu.

## Test Steps

### Edit pada batch terkunci membuka dialog Draft Is Being Edited
1. Ketik Search `Gudang Terkunci {runId}`, tekan Enter
2. Klik row action `Edit` pada baris
3. Verifikasi dialog `Draft Is Being Edited` tampil sebagai pengganti form Edit
4. Verifikasi isi dialog `Rina W is editing this draft. If you take over, their unsaved changes will be lost. Do you want to take over?`
5. Verifikasi tombol `[View only]` dan `[Take over]` tampil pada dialog

### View only membuka form read-only
6. Klik `[View only]`
7. Verifikasi form Register Asset batch `Gudang Terkunci {runId}` terbuka read-only, data tampil sebagai teks atau Badge statis
8. Verifikasi footer form menampilkan `[Close]`
9. Verifikasi tombol `[Save draft]` dan `[Submit]` tidak tampil
10. Klik `[Close]`

### Esc pada dialog Draft Is Being Edited setara View only
11. Klik row action `Edit` pada baris
12. Verifikasi dialog `Draft Is Being Edited` tampil
13. Tekan `Esc`
14. Verifikasi form Register Asset terbuka read-only seperti pada View only, dengan footer `[Close]`
15. Klik `[Close]`

### Delete batch terkunci ditolak dengan dialog blok
16. Klik row action `Delete` pada baris
17. Verifikasi dialog blok `Draft Is Being Edited` tampil
18. Verifikasi teks dialog `Rina W is editing this draft. It can't be deleted right now.`
19. Verifikasi tombol `[OK]` tampil pada dialog
20. Klik `[OK]`
21. Verifikasi baris `Gudang Terkunci {runId}` tetap tampil di tabel Draft, tidak ada yang dihapus

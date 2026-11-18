---
id: TC-FA-MYASSET-BE-204-confirm-handover-penugasan-aturan-server-dep-assignment
title: "Aturan server Confirm Handover penugasan: hanya selama sesi Handover, validasi, dan aset tidak tercentang"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["FI-05", "T-MYA-01", "V-04", "§1.2#r68", "§1.2#r71", "§9.2#r27", "§9.4.2#r54", "§9.4.3#b9", "§9.6#r10"]
smoke: []
dependsOn: ["Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"]
trace:
  "FI-05": [29, 31]
  "T-MYA-01": [3, 18, 20, 22, 29, 31, 37, 44]
  "V-04": [8, 18, 20, 22, 24, 34, 37]
  "§1.2#r68": [2, 3, 6, 12, 41, 48]
  "§1.2#r71": 29
  "§9.2#r27": [8, 10, 26, 28]
  "§9.4.2#r54": [39, 46]
  "§9.4.3#b9": [3, 13, 41, 48]
  "§9.6#r10": [13, 16]
owner: BE
---

# Aturan server Confirm Handover penugasan: hanya selama sesi Handover, validasi, dan aset tidak tercentang

## Prerequisites
- Aktor: Tono (Assignee Employee) dan Rina (Aktor Assignment yang menekan `[Request Confirmation]` dan membatalkan sesi Handover).
- Data:
  - DU-204-1: User `Tono Wibowo {runId}`, role Read Only, cakupan Group `Head Office` beserta Group di bawahnya, Assignee pada DU-204-3 sampai DU-204-8.
  - DU-204-2: User `Rina Wulandari {runId}`, role Asset Admin, cakupan Group `Head Office` beserta Group di bawahnya, Aktor Assignment Group `Head Office`.
  - DU-204-3: Penugasan Tono dengan Need recipient confirmation `Yes`, aset `Laptop Dell Latitude 5420 - 41 {runId}`, Group `Head Office`, status `Waiting for Handover`, sesi Handover belum dimulai, jendela konfirmasi belum habis setelah sesi dimulai.
  - DU-204-4: Penugasan Tono dengan Need recipient confirmation `Yes` dan sesi Handover berjalan yang menunggu konfirmasi, berisi tiga aset: `Laptop Dell Latitude 5420 - 42 {runId}`, `Laptop Dell Latitude 5420 - 43 {runId}`, dan `Laptop Dell Latitude 5420 - 44 {runId}`, Group `Head Office`, ketiganya berstatus `Waiting for Handover`, jendela konfirmasi belum habis.
  - DU-204-5: Penugasan Tono dengan Need recipient confirmation `Yes` dan sesi Handover berjalan yang menunggu konfirmasi, aset `Laptop Dell Latitude 5420 - 45 {runId}`, Group `Head Office`, status `Waiting for Handover`, jendela konfirmasi belum habis.
  - DU-204-6: Penugasan Tono dengan Need recipient confirmation `Yes` dan sesi Handover berjalan yang menunggu konfirmasi, aset `Laptop Dell Latitude 5420 - 46 {runId}`, Group `Head Office`, status `Waiting for Handover`, Expires At sesi: T0 + lama jendela konfirmasi, dengan T0 waktu sesi dimulai.
  - DU-204-7: Penugasan Tono dengan Need recipient confirmation `Yes` dan sesi Handover berjalan yang menunggu konfirmasi, aset `Laptop Dell Latitude 5420 - 47 {runId}`, Group `Head Office`, status `Waiting for Handover`, jendela konfirmasi belum habis.
  - DU-204-8: Penugasan Tono dengan Need recipient confirmation `Yes` dan sesi Handover berjalan yang menunggu konfirmasi, aset `Laptop Dell Latitude 5420 - 48 {runId}`, Group `Head Office`, status `Waiting for Handover`, Expires At sesi: T0 + lama jendela konfirmasi, dengan T0 waktu sesi dimulai.

## Test Steps

### Task Confirm Handover hanya ada selama sesi Handover aktif dan hilang sesudah Confirm
1. Tono meminta data tab Task
2. Verifikasi data memuat Task Confirm Handover penugasan untuk sesi yang berisi aset `Laptop Dell Latitude 5420 - 42 {runId}`
3. Verifikasi data tidak memuat Task Confirm Handover penugasan untuk aset `Laptop Dell Latitude 5420 - 41 {runId}` sebelum Rina menekan `[Request Confirmation]`
4. Rina menekan `[Request Confirmation]` pada Handover penugasan DU-204-3
5. Tono meminta data tab Task
6. Verifikasi data memuat Task Confirm Handover penugasan untuk aset `Laptop Dell Latitude 5420 - 41 {runId}`
7. Tono mengirim Confirm untuk sesi DU-204-3 dengan aset `Laptop Dell Latitude 5420 - 41 {runId}` dan pernyataan tercentang
8. Verifikasi konfirmasi diterima server
9. Tono meminta data tab Assigned
10. Verifikasi baris penugasan aset `Laptop Dell Latitude 5420 - 41 {runId}` berstatus `Assigned`
11. Tono meminta data tab Task
12. Verifikasi data memuat Task Confirm Handover penugasan untuk sesi yang berisi aset `Laptop Dell Latitude 5420 - 42 {runId}`
13. Verifikasi data tidak memuat Task Confirm Handover penugasan untuk aset `Laptop Dell Latitude 5420 - 41 {runId}`
14. Tono mengirim Confirm kedua untuk sesi DU-204-3 dengan aset `Laptop Dell Latitude 5420 - 41 {runId}` dan pernyataan tercentang
15. Tono meminta Assignment Log baris penugasan aset `Laptop Dell Latitude 5420 - 41 {runId}`
16. Verifikasi Assignment Log memuat satu entri konfirmasi untuk sesi DU-204-3

### Confirm tanpa aset tercentang atau tanpa pernyataan ditolak
17. Tono mengirim Confirm untuk sesi DU-204-5 tanpa aset tercentang dan dengan pernyataan tercentang
18. Verifikasi konfirmasi ditolak server karena belum ada aset tercentang
19. Tono mengirim Confirm untuk sesi DU-204-5 dengan aset `Laptop Dell Latitude 5420 - 45 {runId}` tercentang dan tanpa pernyataan tercentang
20. Verifikasi konfirmasi ditolak server karena pernyataan belum dicentang
21. Tono mengirim Confirm untuk sesi DU-204-5 tanpa aset tercentang dan tanpa pernyataan tercentang
22. Verifikasi konfirmasi ditolak server karena belum ada aset dan pernyataan yang dicentang
23. Tono meminta data tab Assigned
24. Verifikasi baris penugasan aset `Laptop Dell Latitude 5420 - 45 {runId}` tetap berstatus `Waiting for Handover`

### Aset tidak tercentang tetap Waiting for Handover dan tercatat di Assignment Log
25. Tono mengirim Confirm untuk sesi DU-204-4 dengan aset `Laptop Dell Latitude 5420 - 42 {runId}` dan `Laptop Dell Latitude 5420 - 43 {runId}` tercentang, aset `Laptop Dell Latitude 5420 - 44 {runId}` tidak tercentang, dan pernyataan tercentang
26. Verifikasi konfirmasi diterima server
27. Tono meminta data tab Assigned
28. Verifikasi baris penugasan aset `Laptop Dell Latitude 5420 - 42 {runId}` dan `Laptop Dell Latitude 5420 - 43 {runId}` berstatus `Assigned`
29. Verifikasi baris penugasan aset `Laptop Dell Latitude 5420 - 44 {runId}` tetap berstatus `Waiting for Handover`
30. Tono meminta Assignment Log baris penugasan aset `Laptop Dell Latitude 5420 - 44 {runId}`
31. Verifikasi Assignment Log memuat node `Confirmation not received` dengan keterangan `Not received`

### Batas Expires At: sebelum batas diterima, tepat pada batas ditolak
32. Waktu berlalu sampai satu detik sebelum Expires At sesi DU-204-8
33. Tono mengirim Confirm untuk sesi DU-204-8 dengan aset `Laptop Dell Latitude 5420 - 48 {runId}` dan pernyataan tercentang
34. Verifikasi konfirmasi sebelum Expires At diterima server
35. Waktu berlalu sampai tepat Expires At sesi DU-204-6
36. Tono mengirim Confirm untuk sesi DU-204-6 dengan aset `Laptop Dell Latitude 5420 - 46 {runId}` dan pernyataan tercentang
37. Verifikasi konfirmasi pada Expires At ditolak server karena jendela konfirmasi habis
38. Tono meminta data tab Assigned
39. Verifikasi baris penugasan aset `Laptop Dell Latitude 5420 - 46 {runId}` tetap berstatus `Waiting for Handover`
40. Tono meminta data tab Task
41. Verifikasi data tidak memuat Task Confirm Handover penugasan untuk aset `Laptop Dell Latitude 5420 - 46 {runId}`

### Confirm sesudah sesi Handover dibatalkan Aktor ditolak
42. Rina membatalkan sesi Handover DU-204-7
43. Tono mengirim Confirm untuk sesi DU-204-7 dengan aset `Laptop Dell Latitude 5420 - 47 {runId}` dan pernyataan tercentang
44. Verifikasi konfirmasi ditolak server karena sesi Handover sudah dibatalkan
45. Tono meminta data tab Assigned
46. Verifikasi baris penugasan aset `Laptop Dell Latitude 5420 - 47 {runId}` tetap berstatus `Waiting for Handover`
47. Tono meminta data tab Task
48. Verifikasi data tidak memuat Task Confirm Handover penugasan untuk aset `Laptop Dell Latitude 5420 - 47 {runId}`

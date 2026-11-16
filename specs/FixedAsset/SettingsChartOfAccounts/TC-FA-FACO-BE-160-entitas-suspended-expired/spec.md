---
id: TC-FA-FACO-BE-160-entitas-suspended-expired
title: "Server menolak aksi tulis saat entitas Suspended atau Expired"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["§9.4.2#r28", EB-AKS-7]
smoke: []
dependsOn: []
trace:
  "§9.4.2#r28": [3, 5, 7, 9, 11, 13, 15, 16, 21, 23, 25, 27, 29, 31, 33, 34]
  EB-AKS-7: [3, 5, 7, 9, 11, 13, 15, 18, 21, 23, 25, 27, 29, 31, 33, 36]
---

# Server menolak aksi tulis saat entitas Suspended atau Expired

## Prerequisites
- Aktor: Admin S (DU-160-1) pada client yang Suspended dan Admin E (DU-160-2) pada client yang Expired, keduanya Total Control dengan cakupan seluruh client masing-masing.
- Data:
  - DU-160-1: User `Maya Tertangguh {runId}`, Access Level `Total Control`, cakupan seluruh client yang Suspended.
  - DU-160-2: User `Budi Kedaluwarsa {runId}`, Access Level `Total Control`, cakupan seluruh client yang Expired.
  - DU-160-3: Client `Klien Suspended {runId}`, berstatus `Suspended`.
  - DU-160-4: Client `Klien Expired {runId}`, berstatus `Expired`.
  - DU-160-5: Account Code `SUA-{runId}`, Account Name `Kas Awal Suspended {runId}`, Account Function `Asset Cost`, Status `Active`, pada client Suspended.
  - DU-160-6: Account Code `SUB-{runId}`, Account Name `Kas Nonaktif Suspended {runId}`, Account Function `Asset Cost`, Status `Inactive`, pada client Suspended.
  - DU-160-7: Account Code `SUC-{runId}`, Account Name `Kas Ketiga Suspended {runId}`, Account Function `Asset Cost`, Status `Active`, pada client Suspended.
  - DU-160-8: Account Code `EXA-{runId}`, Account Name `Kas Awal Expired {runId}`, Account Function `Asset Cost`, Status `Active`, pada client Expired.
  - DU-160-9: Account Code `EXB-{runId}`, Account Name `Kas Nonaktif Expired {runId}`, Account Function `Asset Cost`, Status `Inactive`, pada client Expired.
  - DU-160-10: Account Code `EXC-{runId}`, Account Name `Kas Ketiga Expired {runId}`, Account Function `Asset Cost`, Status `Active`, pada client Expired.
  - DU-160-11: Account Code `SUN-{runId}`, Account Name `Kas Baru Suspended {runId}`, Account Function `Asset Cost`, input Create pada client Suspended yang tidak boleh tersimpan.
  - DU-160-12: Account Code `EXN-{runId}`, Account Name `Kas Baru Expired {runId}`, Account Function `Asset Cost`, input Create pada client Expired yang tidak boleh tersimpan.
- Kondisi:
  - Kedua client adalah client khusus spec ini; status Suspended dan Expired ditetapkan pada client, bukan pada aktor, dan akun di atas dibuat sebelum status itu berlaku.
  - Semua akun belum pernah diekspor dan tidak dipakai Asset Class (Used By 0), sehingga satu-satunya penghalang aksi tulis adalah status client.

## Test Steps

### Client Suspended menolak seluruh aksi tulis walau aktor punya capability penuh
1. Admin S (DU-160-1) mencatat jumlah entri log akun `SUA-{runId}`, `SUB-{runId}`, dan `SUC-{runId}` pada Changelog, pada System Log milik aktor, dan pada Activity Log
2. Admin S (DU-160-1) mengirim Create dengan Account Code `SUN-{runId}`, Account Name `Kas Baru Suspended {runId}`, dan Account Function `Asset Cost`
3. Verifikasi Create ditolak (Forbidden) dan tidak ada akun dengan Account Code `SUN-{runId}`
4. Admin S (DU-160-1) mengirim Edit akun `SUA-{runId}` dengan Account Name `Kas Diubah Suspended {runId}`
5. Verifikasi Edit ditolak (Forbidden) dan akun `SUA-{runId}` tetap memakai Account Name `Kas Awal Suspended {runId}`
6. Admin S (DU-160-1) mengirim Deactivate atas akun `SUA-{runId}` yang Active
7. Verifikasi Deactivate ditolak (Forbidden) dan akun `SUA-{runId}` tetap `Active`
8. Admin S (DU-160-1) mengirim Activate atas akun `SUB-{runId}` yang Inactive
9. Verifikasi Activate ditolak (Forbidden) dan akun `SUB-{runId}` tetap `Inactive`
10. Admin S (DU-160-1) mengirim Deactivate bulk atas akun `SUA-{runId}` dan `SUC-{runId}`
11. Verifikasi permintaan bulk ditolak (Forbidden) seluruhnya, sehingga akun `SUA-{runId}` dan `SUC-{runId}` tetap `Active`
12. Admin S (DU-160-1) mengirim Delete atas akun `SUB-{runId}`
13. Verifikasi Delete ditolak (Forbidden) dan akun `SUB-{runId}` masih ada
14. Admin S (DU-160-1) mengirim Delete bulk atas akun `SUA-{runId}` dan `SUC-{runId}`
15. Verifikasi Delete bulk ditolak (Forbidden) seluruhnya dan akun `SUA-{runId}` serta `SUC-{runId}` masih ada
16. Verifikasi jumlah entri log ketiga akun dan akun `SUN-{runId}` tidak bertambah pada ketiga surface, sehingga penolakan tidak meninggalkan log
17. Admin S (DU-160-1) mengirim permintaan daftar akun client
18. Verifikasi permintaan baca tetap berhasil dan daftar memuat akun `SUA-{runId}`, `SUB-{runId}`, dan `SUC-{runId}`, karena penolakan hanya berlaku bagi aksi tulis

### Client Expired menolak seluruh aksi tulis walau aktor punya capability penuh
19. Admin E (DU-160-2) mencatat jumlah entri log akun `EXA-{runId}`, `EXB-{runId}`, dan `EXC-{runId}` pada Changelog, pada System Log milik aktor, dan pada Activity Log
20. Admin E (DU-160-2) mengirim Create dengan Account Code `EXN-{runId}`, Account Name `Kas Baru Expired {runId}`, dan Account Function `Asset Cost`
21. Verifikasi Create ditolak (Forbidden) dan tidak ada akun dengan Account Code `EXN-{runId}`
22. Admin E (DU-160-2) mengirim Edit akun `EXA-{runId}` dengan Account Name `Kas Diubah Expired {runId}`
23. Verifikasi Edit ditolak (Forbidden) dan akun `EXA-{runId}` tetap memakai Account Name `Kas Awal Expired {runId}`
24. Admin E (DU-160-2) mengirim Deactivate atas akun `EXA-{runId}` yang Active
25. Verifikasi Deactivate ditolak (Forbidden) dan akun `EXA-{runId}` tetap `Active`
26. Admin E (DU-160-2) mengirim Activate atas akun `EXB-{runId}` yang Inactive
27. Verifikasi Activate ditolak (Forbidden) dan akun `EXB-{runId}` tetap `Inactive`
28. Admin E (DU-160-2) mengirim Deactivate bulk atas akun `EXA-{runId}` dan `EXC-{runId}`
29. Verifikasi permintaan bulk ditolak (Forbidden) seluruhnya, sehingga akun `EXA-{runId}` dan `EXC-{runId}` tetap `Active`
30. Admin E (DU-160-2) mengirim Delete atas akun `EXB-{runId}`
31. Verifikasi Delete ditolak (Forbidden) dan akun `EXB-{runId}` masih ada
32. Admin E (DU-160-2) mengirim Delete bulk atas akun `EXA-{runId}` dan `EXC-{runId}`
33. Verifikasi Delete bulk ditolak (Forbidden) seluruhnya dan akun `EXA-{runId}` serta `EXC-{runId}` masih ada
34. Verifikasi jumlah entri log ketiga akun dan akun `EXN-{runId}` tidak bertambah pada ketiga surface, sehingga penolakan tidak meninggalkan log
35. Admin E (DU-160-2) mengirim permintaan daftar akun client
36. Verifikasi permintaan baca tetap berhasil dan daftar memuat akun `EXA-{runId}`, `EXB-{runId}`, dan `EXC-{runId}`, karena penolakan hanya berlaku bagi aksi tulis

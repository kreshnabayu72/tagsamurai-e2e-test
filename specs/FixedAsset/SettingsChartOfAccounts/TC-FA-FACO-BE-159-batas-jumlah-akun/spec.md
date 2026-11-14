---
id: TC-FA-FACO-BE-159-batas-jumlah-akun
title: "Batas jumlah akun pada Create Account"
layer: be-e2e
priority: Medium
caseType: Negative
status: draft
owner: BE
sourceRules: [FACO-LOGIC-10a, FACO-LOGIC-10b, FACO-LOGIC-10d, "§[F-FACO-01] Create Account#r6", "§9.4.2#r39", EB-CON-4]
smoke: []
dependsOn: []
trace:
  FACO-LOGIC-10a: [11, 14]
  FACO-LOGIC-10b: [6, 23, 27]
  FACO-LOGIC-10d: [6, 7, 8, 11, 19]
  "§[F-FACO-01] Create Account#r6": [6, 7, 8, 18, 19]
  "§9.4.2#r39": [18, 19]
  EB-CON-4: [3, 6, 7, 11, 14, 18]
---

# Batas jumlah akun pada Create Account

## Prerequisites
- Aktor: Admin A (DU-159-1) dan Admin B (DU-159-2), keduanya Total Control dengan cakupan seluruh client khusus spec ini; operator platform yang mengubah plan client khusus.
- Data:
  - DU-159-1: User `Maya Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client khusus.
  - DU-159-2: User `Budi Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client khusus.
  - DU-159-3: akun pengisi Active dengan Account Code `PGA{n}-{runId}` dan Account Name `Kas Pengisi Aktif {n} {runId}`, Account Function `Asset Cost`, sejumlah batas dikurangi tiga.
  - DU-159-4: Account Code `LIM3-{runId}`, Account Name `Kas Calon Nonaktif {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-159-5: Account Code `PGI-{runId}`, Account Name `Kas Pengisi Nonaktif {runId}`, Account Function `Asset Cost`, Status `Inactive`.
- Kondisi:
  - Client khusus spec ini berplan Enterprise pada awal spec, dan Master Data Count Limit yang berlaku padanya adalah batas jumlah akun semua status (dalam skenario ditulis "batas").
  - Nilai batas tidak dinyatakan di PRD maupun foundation, sehingga langkah memakai keadaan relatif terhadap batas (satu di bawah batas dan tepat sama dengan batas) tanpa angka.
  - Pada awal spec total akun client sama dengan batas dikurangi satu: akun DU-159-3, DU-159-4, dan DU-159-5 adalah seluruh akun client.
  - Semua akun di atas belum pernah diekspor dan tidak dipakai Asset Class (Used By 0), sehingga Deactivate dan Delete tidak diblokir.

## Test Steps

### Create pada total akun satu di bawah batas berhasil
1. Admin A mencatat total seluruh akun client, semua status
2. Admin A mengirim Create dengan Account Code `LIM1-{runId}`, Account Name `Kas Batas Terakhir {runId}`, dan Account Function `Asset Cost`, ketika total akun client satu di bawah batas
3. Verifikasi akun `LIM1-{runId}` tersimpan, total akun client naik satu dan kini tepat sama dengan batas, dan akun itu memiliki tepat satu entri log Create pada masing-masing dari ketiga surface

### Create ketika total akun tepat sama dengan batas ditolak tanpa mutasi dan tanpa log
4. Admin A mencatat total seluruh akun client dan jumlah entri log akun `LIM2-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
5. Admin A mengirim Create dengan Account Code `LIM2-{runId}`, Account Name `Kas Melebihi Batas {runId}`, dan Account Function `Asset Cost`
6. Verifikasi Create ditolak karena batas jumlah akun client tercapai, meskipun client berplan Enterprise
7. Verifikasi tidak ada akun dengan Account Code `LIM2-{runId}` dan total akun client tidak berubah, sehingga penolakan tidak meninggalkan mutasi
8. Verifikasi jumlah entri log akun `LIM2-{runId}` tidak bertambah pada ketiga surface, sehingga penolakan tidak meninggalkan log

### Akun berstatus Inactive ikut dihitung dalam total
9. Admin A mengirim Deactivate atas akun `LIM3-{runId}`, akun yang boleh dinonaktifkan
10. Admin A mengirim Create dengan Account Code `LIM4-{runId}`, Account Name `Kas Setelah Nonaktif {runId}`, dan Account Function `Asset Cost`
11. Verifikasi Create ditolak karena batas tercapai walau satu akun kini Inactive, sehingga akun Inactive tetap dihitung, dan tidak ada akun dengan Account Code `LIM4-{runId}`

### Delete membebaskan satu slot
12. Admin A mengirim Delete atas akun `LIM3-{runId}`
13. Admin A mengirim Create dengan Account Code `LIM4-{runId}`, Account Name `Kas Setelah Nonaktif {runId}`, dan Account Function `Asset Cost`
14. Verifikasi akun `LIM4-{runId}` tersimpan dan total akun client kembali tepat sama dengan batas

### Dua admin berebut slot terakhir
15. Admin A mengirim Delete atas akun `LIM4-{runId}`, sehingga total akun client kembali satu di bawah batas
16. Admin A mencatat jumlah entri log akun `LIM5-{runId}` dan `LIM6-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
17. Admin A mengirim Create dengan Account Code `LIM5-{runId}`, Account Name `Kas Rebutan Satu {runId}`, dan Account Function `Asset Cost`, serentak dengan Admin B yang mengirim Create dengan Account Code `LIM6-{runId}`, Account Name `Kas Rebutan Dua {runId}`, dan Account Function `Asset Cost`
18. Verifikasi tepat satu dari kedua Create berhasil: tepat satu di antara akun `LIM5-{runId}` dan akun `LIM6-{runId}` ada, dan total akun client tepat sama dengan batas, bukan melebihinya
19. Verifikasi Create yang kalah ditolak karena batas tercapai antara klik dan Submit, tanpa akun tersimpan dan tanpa entri log baru pada ketiga surface untuk akunnya

### Batas berlaku juga pada plan Growth dan Professional
20. Operator platform mengubah plan client khusus menjadi Growth, sementara total akun client tetap tepat sama dengan batas
21. Admin A mencatat total seluruh akun client
22. Admin A mengirim Create dengan Account Code `LIM7-{runId}`, Account Name `Kas Plan Growth {runId}`, dan Account Function `Asset Cost`
23. Verifikasi Create ditolak karena batas jumlah akun client tercapai pada plan Growth, tidak ada akun dengan Account Code `LIM7-{runId}`, dan total akun client tidak berubah
24. Operator platform mengubah plan client khusus menjadi Professional, sementara total akun client tetap tepat sama dengan batas
25. Admin A mencatat total seluruh akun client
26. Admin A mengirim Create dengan Account Code `LIM8-{runId}`, Account Name `Kas Plan Professional {runId}`, dan Account Function `Asset Cost`
27. Verifikasi Create ditolak karena batas jumlah akun client tercapai pada plan Professional, tidak ada akun dengan Account Code `LIM8-{runId}`, dan total akun client tidak berubah

---
id: TC-FA-FATR-BE-128-aturan-audit-dep-audit
title: "Grace period, Require approval, dan Require location pada task Audit"
layer: be-e2e
priority: High
caseType: Negative
status: ready-for-automation
sourceRules: ["§4.1#r226", "§4.1#r227", "§4.1#r228", "§Aturan Logika Modul#r126", "§9.2#b564", "§4.1#r198", "§9.2#b565", "§9.4.2#r68", "§9.4.2#r65", "§Aturan Logika Modul#r111", "§4.1#r239", "§4.1#r240", "§9.2#b560", "§Aturan Logika Modul#r114", "§Aturan Logika Modul#r108", "§Aturan Logika Modul#r117", "§11#r19", "EB-XM-2@audit", "§Aturan Logika Modul#r112"]
smoke: []
dependsOn:
  - "Audit: task Audit, Finish Audit, dan perekaman lokasi"
owner: BE
trace:
  "§4.1#r226": [6, 10]
  "§4.1#r227": [7, 8]
  "§4.1#r228": [6, 7]
  "§Aturan Logika Modul#r126": [6, 7]
  "§9.2#b564": [6, 7]
  "§4.1#r198": [14, 17]
  "§9.2#b565": [14, 17]
  "§9.4.2#r68": [7, 8]
  "§9.4.2#r65": 26
  "§Aturan Logika Modul#r111": [26, 27, 31]
  "§4.1#r239": [26, 32]
  "§4.1#r240": [20, 21, 37, 38]
  "§9.2#b560": [26, 27, 29]
  "§Aturan Logika Modul#r114": 26
  "§Aturan Logika Modul#r108": 29
  "§Aturan Logika Modul#r117": [7, 8]
  "§11#r19": [6, 14, 26]
  "EB-XM-2@audit": 17
  "§Aturan Logika Modul#r112": [32, 33]
anchor: []
---

# Grace period, Require approval, dan Require location pada task Audit

## Prerequisites
- Aktor: Admin `Dewi Lestari {runId}` (Total Control entitas khusus; mengubah setting Transaction Settings dan membuat task Audit); Auditor `Eko Prasetyo {runId}` (ditugaskan pada semua task Audit di spec ini; menjalankan Finish Audit).
- Data:
  - DU-128-1: Entitas `Citra Aturan Audit {runId}`, entitas khusus yang hanya dipakai spec ini dan tidak dipakai spec lain. Plan-nya menyediakan Approval Workflow, dan addon Audit aktif pada subscription FAMS-nya.
  - DU-128-2: User `Dewi Lestari {runId}`, Role `Total Control entitas`; Admin yang mengubah setting.
  - DU-128-3: User `Eko Prasetyo {runId}`, Role `Employee`; Auditor yang ditugaskan pada task Audit.
  - DU-128-4: Category `Laptop {runId}`; Category leaf.
  - DU-128-5: Category `Genset {runId}`; Category leaf.
  - DU-128-6: Asset `Lenovo ThinkPad E14 {runId}`, Category `Laptop {runId}`; aset task Audit sebelum perubahan Grace period.
  - DU-128-7: Asset `Dell Latitude 5440 {runId}`, Category `Laptop {runId}`; aset task Audit sesudah perubahan Grace period.
  - DU-128-8: Asset `Genset Perkins 20kVA {runId}`, Category `Genset {runId}`; aset task Audit sesudah perubahan Grace period.
  - DU-128-9: Asset `HP ProBook 450 {runId}`, Category `Laptop {runId}`; aset task Audit untuk Require approval `ON`.
  - DU-128-10: Asset `Genset Cummins 30kVA {runId}`, Category `Genset {runId}`; aset task Audit untuk Require approval `OFF`.
  - DU-128-11: Asset `Asus ExpertBook B1 {runId}`, Category `Laptop {runId}`; aset task Audit saat Require location `OFF`.
  - DU-128-12: Asset `Acer Aspire 5 {runId}`, Category `Laptop {runId}`; aset task Audit saat Require location `ON`.
  - DU-128-13: Asset `Genset Kohler 15kVA {runId}`, Category `Genset {runId}`; aset task Audit saat Require location `ON` pada Category lain.
  - DU-128-14: Task Audit `Audit Laptop Lama {runId}`, aset `Lenovo ThinkPad E14 {runId}`, durasi `1` hari; dibuat sebelum Grace period diubah.
  - DU-128-15: Task Audit `Audit Laptop Baru {runId}`, aset `Dell Latitude 5440 {runId}`, durasi `1` hari; dibuat sesudah Grace period diubah.
  - DU-128-16: Task Audit `Audit Genset Baru {runId}`, aset `Genset Perkins 20kVA {runId}`, durasi `1` hari; dibuat sesudah Grace period diubah.
  - DU-128-17: Task Audit `Audit Approval Laptop {runId}`, aset `HP ProBook 450 {runId}`, durasi `1` hari.
  - DU-128-18: Task Audit `Audit Approval Genset {runId}`, aset `Genset Cummins 30kVA {runId}`, durasi `1` hari.
  - DU-128-19: Task Audit `Audit Lokasi OFF {runId}`, aset `Asus ExpertBook B1 {runId}`, durasi `1` hari.
  - DU-128-20: Task Audit `Audit Lokasi ON Laptop {runId}`, aset `Acer Aspire 5 {runId}`, durasi `1` hari.
  - DU-128-21: Task Audit `Audit Lokasi ON Genset {runId}`, aset `Genset Kohler 15kVA {runId}`, durasi `1` hari.
  - DU-128-22: Perubahan Company default tab Audit: Grace period `0`.
  - DU-128-23: Perubahan Company default tab Audit: Require approval `OFF`.
  - DU-128-24: Perubahan Company default tab Geolocation: Require location Audit `ON`.
  - DU-128-25: Data lokasi perangkat Auditor: koordinat `-6.2088, 106.8456`, akurasi `10` meter.
  - DU-128-26: Asset `Toshiba Dynabook R40 {runId}`, Category `Laptop {runId}`; aset task Audit saat Require location `OFF` dan Auditor mengirim data lokasi.
  - DU-128-27: Task Audit `Audit Lokasi OFF Terkirim {runId}`, aset `Toshiba Dynabook R40 {runId}`, durasi `1` hari.
  - DU-128-28: Perubahan Company default tab Geolocation: Require location Audit `OFF`.
- Kondisi:
  - Company default entitas DU-128-1 saat spec mulai: Grace period `3`, Require approval Audit `ON`, Require location Audit `OFF`.
  - Akun Admin `Dewi Lestari {runId}` dan Auditor `Eko Prasetyo {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Grace period di-snapshot pada task saat task dibuat
1. Admin `Dewi Lestari {runId}` membuat task Audit `Audit Laptop Lama {runId}` untuk aset `Lenovo ThinkPad E14 {runId}` dengan durasi `1` hari
2. Admin menyimpan Company default tab Audit dengan Grace period `0`
3. Admin membuat task Audit `Audit Laptop Baru {runId}` untuk aset `Dell Latitude 5440 {runId}` dengan durasi `1` hari
4. Admin membuat task Audit `Audit Genset Baru {runId}` untuk aset `Genset Perkins 20kVA {runId}` dengan durasi `1` hari
5. Waktu berlalu sampai durasi ketiga task Audit berakhir
6. Verifikasi task `Audit Laptop Lama {runId}` berstatus `Grace Period` dan bukan `Overdue`, karena Grace period `3` yang berlaku saat task dibuat tidak terpengaruh perubahan ke `0`
7. Verifikasi task `Audit Laptop Baru {runId}` langsung berstatus `Overdue` tanpa status `Grace Period`
8. Verifikasi task `Audit Genset Baru {runId}` pada Category `Genset {runId}` juga langsung berstatus `Overdue` tanpa status `Grace Period`

### Task lama menjadi Overdue setelah tenggang 3 hari lewat
9. Waktu berlalu sampai 4 hari sesudah durasi task `Audit Laptop Lama {runId}` berakhir
10. Verifikasi task `Audit Laptop Lama {runId}` berstatus `Overdue` karena tenggang Grace period `3` hari sudah lewat

### Require approval Audit dibaca saat Finish Audit
11. Admin membuat task Audit `Audit Approval Laptop {runId}` untuk aset `HP ProBook 450 {runId}` dengan durasi `1` hari
12. Admin membuat task Audit `Audit Approval Genset {runId}` untuk aset `Genset Cummins 30kVA {runId}` dengan durasi `1` hari
13. Auditor `Eko Prasetyo {runId}` menjalankan Finish Audit pada task `Audit Approval Laptop {runId}`
14. Verifikasi task `Audit Approval Laptop {runId}` berstatus `Waiting for Approval` dan bukan `Completed`, karena Require approval Audit `ON`
15. Admin menyimpan Company default tab Audit dengan Require approval `OFF`
16. Auditor menjalankan Finish Audit pada task `Audit Approval Genset {runId}`, yang dibuat saat Require approval Audit `ON`
17. Verifikasi task `Audit Approval Genset {runId}` langsung berstatus `Completed`, karena Require approval Audit `OFF` dibaca saat Finish Audit

### Require location OFF tidak merekam lokasi
18. Admin membuat task Audit `Audit Lokasi OFF {runId}` untuk aset `Asus ExpertBook B1 {runId}` dengan durasi `1` hari
19. Auditor menjalankan Finish Audit pada task `Audit Lokasi OFF {runId}` tanpa data lokasi
20. Verifikasi Finish Audit task `Audit Lokasi OFF {runId}` diterima
21. Verifikasi tidak ada data lokasi tercatat pada task `Audit Lokasi OFF {runId}`

### Require location ON mewajibkan lokasi pada task Audit yang dibuat sesudahnya
22. Admin menyimpan Company default tab Geolocation dengan Require location Audit `ON`
23. Admin membuat task Audit `Audit Lokasi ON Laptop {runId}` untuk aset `Acer Aspire 5 {runId}` dengan durasi `1` hari
24. Admin membuat task Audit `Audit Lokasi ON Genset {runId}` untuk aset `Genset Kohler 15kVA {runId}` dengan durasi `1` hari
25. Auditor menjalankan Finish Audit pada task `Audit Lokasi ON Laptop {runId}` tanpa data lokasi
26. Verifikasi Finish Audit task `Audit Lokasi ON Laptop {runId}` ditolak karena Require location Audit `ON` mewajibkan data lokasi
27. Verifikasi task `Audit Lokasi ON Laptop {runId}` tidak berubah menjadi selesai
28. Auditor menjalankan Finish Audit pada task `Audit Lokasi ON Genset {runId}` tanpa data lokasi
29. Verifikasi Finish Audit task `Audit Lokasi ON Genset {runId}` pada Category `Genset {runId}` ditolak karena Require location Audit `ON` mewajibkan data lokasi
30. Auditor menjalankan Finish Audit pada task `Audit Lokasi ON Laptop {runId}` dengan data lokasi koordinat `-6.2088, 106.8456` dan akurasi `10` meter
31. Verifikasi Finish Audit task `Audit Lokasi ON Laptop {runId}` diterima
32. Verifikasi data lokasi koordinat `-6.2088, 106.8456` dengan akurasi `10` meter tercatat pada task `Audit Lokasi ON Laptop {runId}`
33. Verifikasi waktu perekaman lokasi dari Finish Audit itu tercatat pada task `Audit Lokasi ON Laptop {runId}`

### Require location OFF tidak merekam lokasi yang dikirim Auditor
34. Admin menyimpan Company default tab Geolocation dengan Require location Audit `OFF`
35. Admin membuat task Audit `Audit Lokasi OFF Terkirim {runId}` untuk aset `Toshiba Dynabook R40 {runId}` dengan durasi `1` hari
36. Auditor menjalankan Finish Audit pada task `Audit Lokasi OFF Terkirim {runId}` dengan data lokasi koordinat `-6.2088, 106.8456` dan akurasi `10` meter
37. Verifikasi Finish Audit task `Audit Lokasi OFF Terkirim {runId}` diterima
38. Verifikasi data lokasi koordinat `-6.2088, 106.8456` dengan akurasi `10` meter tidak tercatat pada task `Audit Lokasi OFF Terkirim {runId}`

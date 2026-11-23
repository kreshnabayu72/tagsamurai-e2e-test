---
id: TC-FA-DAMAGED-BE-215-registrasi-approval-on-server
title: "Dengan Approval registrasi aset ON, record Damaged Source Registration dibuat saat Approve atas nama approver dengan Damage note hasil koreksi approver sebagai What happened, dan Return to Draft atau Reject tidak membuat record"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r85", "§Aturan Logika Modul#r87", EC-DMG-28, "§8.1#r7", "§Aturan Logika Modul#r88"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§Aturan Logika Modul#r85": [5]
  "§Aturan Logika Modul#r87": [6]
  EC-DMG-28: [1, 3, 4, 5, 9, 12]
  "§8.1#r7": [6, 7]
  "§Aturan Logika Modul#r88": [9, 10, 12, 13]
---

# Dengan Approval registrasi aset ON, record Damaged Source Registration dibuat saat Approve atas nama approver dengan Damage note hasil koreksi approver sebagai What happened, dan Return to Draft atau Reject tidak membuat record

## Prerequisites
- Aktor:
  - Approver registrasi aset `Wahyu Hidayat {runId}`, berhak Approve, Return to Draft, dan Reject pengajuan registrasi aset, pada Client `Client Approval Registrasi {runId}`.
  - Pengaju registrasi `Siti Rahmawati {runId}`, bukan approver, pada Client `Client Approval Registrasi {runId}`.
- Data:
  - DU-215-1: Client `Client Approval Registrasi {runId}` dengan Approval registrasi aset bernilai `ON`.
  - DU-215-2: User `Wahyu Hidayat {runId}`, approver registrasi aset, cakupan Group `Head Office {runId}`, pada Client `Client Approval Registrasi {runId}`.
  - DU-215-3: User `Siti Rahmawati {runId}`, pengaju registrasi, bukan approver, cakupan Group `Head Office {runId}`, pada Client `Client Approval Registrasi {runId}`.
  - DU-215-4: Aset `Projector Epson EB-X06 - 201 {runId}`, Group `Head Office {runId}`, draf registrasi ber-Condition `Damaged` dengan Damage note `Lensa tergores saat pengiriman {runId}`, sudah diajukan oleh `Siti Rahmawati {runId}` untuk approval, belum Active.
  - DU-215-5: Aset `Projector Epson EB-X06 - 202 {runId}`, Group `Head Office {runId}`, draf registrasi ber-Condition `Damaged` dengan Damage note `Lensa tergores saat pengiriman {runId}`, sudah diajukan oleh `Siti Rahmawati {runId}` untuk approval, belum Active.
  - DU-215-6: Aset `Projector Epson EB-X06 - 203 {runId}`, Group `Head Office {runId}`, draf registrasi ber-Condition `Damaged` dengan Damage note `Lensa tergores saat pengiriman {runId}`, sudah diajukan oleh `Siti Rahmawati {runId}` untuk approval, belum Active.
  - DU-215-7: Damage note hasil koreksi approver `Lensa tergores dan bodi penyok saat pengiriman {runId}`.
- Kondisi:
  - Memakai entitas khusus yang tidak dipakai spec lain: Client `Client Approval Registrasi {runId}`.
  - Approval registrasi aset bernilai `ON` pada Client `Client Approval Registrasi {runId}`.

## Test Steps

### Approve membuat record atas nama approver dengan Damage note hasil koreksi approver
1. Verifikasi pengajuan registrasi `Projector Epson EB-X06 - 201 {runId}` yang sudah diajukan tetapi belum di-Approve belum memiliki Damage record
2. Approver `Wahyu Hidayat {runId}` melakukan Approve atas pengajuan registrasi `Projector Epson EB-X06 - 201 {runId}` dengan mengoreksi Damage note menjadi `Lensa tergores dan bodi penyok saat pengiriman {runId}`
3. Verifikasi server membuat satu record `Damaged` untuk `Projector Epson EB-X06 - 201 {runId}` saat Approve, tanpa Confirm
4. Verifikasi Source record itu adalah `Registration`
5. Verifikasi What happened record sama dengan Damage note hasil koreksi approver `Lensa tergores dan bodi penyok saat pengiriman {runId}`, bukan Damage note awal `Lensa tergores saat pengiriman {runId}`
6. Verifikasi node pertama `Reported damaged by` atas nama approver `Wahyu Hidayat {runId}`, bukan atas nama pengaju `Siti Rahmawati {runId}`
7. Verifikasi record itu tidak memiliki Damaged Photo dan pembuatannya tidak mensyaratkan foto

### Return to Draft tidak membuat record
8. Approver `Wahyu Hidayat {runId}` melakukan Return to Draft atas pengajuan registrasi `Projector Epson EB-X06 - 202 {runId}`
9. Verifikasi tidak ada Damage record untuk `Projector Epson EB-X06 - 202 {runId}`
10. Verifikasi tidak ada node `Reported damaged by` dan tidak ada entri Transaction log aset Reported damaged untuk `Projector Epson EB-X06 - 202 {runId}`

### Reject tidak membuat record
11. Approver `Wahyu Hidayat {runId}` melakukan Reject atas pengajuan registrasi `Projector Epson EB-X06 - 203 {runId}`
12. Verifikasi tidak ada Damage record untuk `Projector Epson EB-X06 - 203 {runId}`
13. Verifikasi tidak ada node `Reported damaged by` dan tidak ada entri Transaction log aset Reported damaged untuk `Projector Epson EB-X06 - 203 {runId}`

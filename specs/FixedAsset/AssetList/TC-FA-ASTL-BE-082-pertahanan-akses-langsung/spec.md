---
id: TC-FA-ASTL-BE-082-pertahanan-akses-langsung
title: "Akses langsung dan tampering ditolak"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [T-07]
smoke: []
dependsOn: []
trace:
  T-07: [2, 4, 6, 8]
anchor: []
---

# Akses langsung dan tampering ditolak

## Prerequisites
- Aktor: Group Manager (Dewi).
- Data:
  - DU-082-1: User, group Manager untuk IT: Name `Dewi Lestari {runId}`, Role `Group Manager`, Cakupan `IT {runId}`.
  - DU-082-2: Group, dua group tanpa induk: Name `IT {runId}`, Group lain `Cabang Bandung {runId}`.
  - DU-082-3: Asset, aset di IT dalam cakupan Dewi sebagai asal permintaan: Name `Laptop Pro 16 - 1 {runId}`, Lifecycle `Active`, Group `IT {runId}`.
  - DU-082-4: Asset, aset di luar cakupan Dewi: Name `Proyektor X2 - 1 {runId}`, Lifecycle `Active`, Group `Cabang Bandung {runId}`, Purchase Cost `15000000.00`.

## Test Steps

### Akses langsung dan tampering ke aset di luar cakupan ditolak
1. Dewi meminta akses langsung ke aset `Proyektor X2 - 1 {runId}` lewat tautan langsung
2. Verifikasi akses ditolak dengan pesan `You don't have permission to do this.` dan respons tidak memuat data aset `Proyektor X2 - 1 {runId}`
3. Dewi mengirim Add Label `Prioritas {runId}` atas aset `Proyektor X2 - 1 {runId}` dengan mengganti penanda aset pada permintaan yang semula untuk `Laptop Pro 16 - 1 {runId}`
4. Verifikasi permintaan ditolak dengan pesan `You don't have permission to do this.` dan `Proyektor X2 - 1 {runId}` tidak berlabel `Prioritas {runId}`
5. Dewi mengirim Edit Purchase atas aset `Proyektor X2 - 1 {runId}` dengan Purchase Cost `12000000.00`, dengan mengganti penanda aset pada permintaan yang semula untuk `Laptop Pro 16 - 1 {runId}`
6. Verifikasi permintaan ditolak dengan pesan `You don't have permission to do this.` dan Purchase Cost `Proyektor X2 - 1 {runId}` tetap `15000000.00`
7. Dewi mengirim Delete Asset Data atas aset `Proyektor X2 - 1 {runId}` dengan mengganti penanda aset pada permintaan yang semula untuk `Laptop Pro 16 - 1 {runId}`
8. Verifikasi permintaan ditolak dengan pesan `You don't have permission to do this.` dan `Proyektor X2 - 1 {runId}` tetap ada

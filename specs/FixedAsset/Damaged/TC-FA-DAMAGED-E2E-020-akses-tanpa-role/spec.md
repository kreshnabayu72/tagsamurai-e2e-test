---
id: TC-FA-DAMAGED-E2E-020-akses-tanpa-role
title: "Pengguna tanpa role Damaged (pelapor umum) tidak melihat tab Damaged dan URL langsung ditolak"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EB-AKS-1, EB-AKS-2, §2.1#b3, §4.8#r1, §2.1#r1, §2#b7]
smoke: []
dependsOn: []
trace:
  EB-AKS-1: 2
  EB-AKS-2: [4, 5, 6]
  §2.1#b3: 2
  §4.8#r1: 2
  §2.1#r1: 5
  §2#b7: 5
anchor: [1]
coverage:
  web: automated
---

# Pengguna tanpa role Damaged (pelapor umum) tidak melihat tab Damaged dan URL langsung ditolak

## Prerequisites
- Aktor: pelapor umum tanpa role Damaged (DU-020-2).
- Layar awal: halaman utama setelah masuk.
- Data:
  - DU-020-1: Damage record aset `Laptop Dell Latitude 5420 {runId}` di Group `Head Office {runId}`, status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan DU-020-2.
  - DU-020-2: User `Budi Santoso {runId}`, pemegang aset `Laptop Dell Latitude 5420 {runId}` yang melapor dari My Asset, tanpa role Damaged dan tanpa capability di tab Damaged; cakupan: aset yang ia pegang.

## Test Steps

### Tab Damaged tidak tersedia bagi pengguna tanpa role
1. Verifikasi item `My Asset` tampil pada sidebar
2. Verifikasi item sidebar `Assets` tidak tampil

### URL langsung ke tab Damaged ditolak
3. Buka alamat tab `Damaged` pada halaman Assets secara langsung
4. Verifikasi toast `You don't have permission to do this.` tampil setelah alamat dibuka langsung
5. Verifikasi sub-tab `Active` dan `History` tidak tampil
6. Verifikasi halaman tidak dialihkan ke halaman lain

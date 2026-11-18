---
id: TC-FA-ASTL-E2E-033-gating-tanpa-akses
title: "Aktor tanpa akses tidak masuk modul"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§4.8#r1", "§4.8#r13", "§4.8#r14", "§2#r5", "§2#r6", "§2#r7", "§2#r8", "§2#r9", "§2#r10", "§2#r11", "§2#r12", "§2#r13", "§2#r14", "§2#r15", "§2#r16", "§2#p3", "EB-AKS-1", "EB-AKS-2"]
smoke: []
dependsOn: []
trace:
  "§4.8#r1": 2
  "§4.8#r13": [4, 5, 6]
  "§4.8#r14": [4, 5, 6]
  "§2#r5": 9
  "§2#r6": 9
  "§2#r7": 9
  "§2#r8": 9
  "§2#r9": 9
  "§2#r10": 9
  "§2#r11": 9
  "§2#r12": 9
  "§2#r13": 9
  "§2#r14": 9
  "§2#r15": 9
  "§2#r16": [2, 4, 5, 6]
  "§2#p3": 9
  "EB-AKS-1": [2, 9]
  "EB-AKS-2": [4, 5, 6]
anchor: [1]
coverage:
  web: automated
---

# Aktor tanpa akses tidak masuk modul

## Prerequisites
- Aktor: `Wulan Prasetyo {runId}`, pemegang role Staff tanpa capability baca untuk modul All Assets.
- Layar awal: Beranda Fixed Asset.
- Data:
  - DU-033-1: User, Name `Wulan Prasetyo {runId}`, Role `Staff`, Cakupan `Tanpa akses ke modul All Assets`
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Lisensi `FA-7` aktif pada entitas.

## Test Steps

### Item menu modul tidak tampil bagi aktor tanpa capability
1. Verifikasi sidebar Fixed Asset menampilkan item menu milik hak aktor
2. Verifikasi item menu `All Assets` tidak dirender (Hidden)

### Akses URL halaman modul ditolak
3. Buka URL halaman All Assets langsung
4. Verifikasi toast `You don't have permission to do this.` tampil
5. Verifikasi aktor tetap berada di halaman semula tanpa redirect
6. Verifikasi tabel dan Sidebar Group tidak dirender (Hidden)

### Aktor dengan capability baca melihat item menu
7. Admin memberi `Wulan Prasetyo {runId}` hak `Read Only`
8. Muat ulang halaman
9. Verifikasi item menu `All Assets` tampil

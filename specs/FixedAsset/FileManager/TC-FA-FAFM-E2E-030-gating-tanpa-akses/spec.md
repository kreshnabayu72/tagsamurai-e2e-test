---
id: TC-FA-FAFM-E2E-030-gating-tanpa-akses
title: "Aktor tanpa akses File Manager: menu tidak tampil dan URL langsung ditolak"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§2#r9", "§9.11#r5", EB-AKS-1, EB-AKS-2]
smoke: []
dependsOn: []
trace:
  "§2#r9": [2, 6]
  "§9.11#r5": [2, 4, 8, 10]
  EB-AKS-1: [2]
  EB-AKS-2: [4, 5, 6, 8, 10]
anchor: [1]
coverage:
  web: automated
---

# Aktor tanpa akses File Manager: menu tidak tampil dan URL langsung ditolak

## Prerequisites
- Aktor: Rahmat Tanpa Akses `{runId}` (tanpa capability File Manager apa pun, dengan akses baca ke modul Fixed Asset lain).
- Layar awal: halaman beranda Fixed Asset, tempat sidebar tampil.
- Data:
  - DU-030-1: User `Rahmat Tanpa Akses {runId}`, role `Pengguna tanpa capability File Manager`, capability File Manager `tidak ada`.
  - DU-030-2: File `bukti-hapus-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}` (Increment dibentuk server), Asset ID milik aset itu, Group `Head Office`, Size `310.0 KB`, Uploaded By `Rina A`, Upload Date `T0 − 20 hari, pukul 09:00`, sudah dihapus permanen sebelum spec dimulai.
  - DU-030-3: File `dokumen-entitas-lain-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Scanner Epson DS-530 {runId}` (Increment dibentuk server), Asset ID milik aset itu, Group `Branch Bandung`, Size `300.0 KB`, Uploaded By `Rina A`, Upload Date `T0 − 12 hari, pukul 08:45`, milik entitas lain, bukan entitas aktor.

## Test Steps

### Item File Manager tidak ada di sidebar
1. Verifikasi sidebar Fixed Asset memuat item modul lain
2. Verifikasi item `File Manager` tidak ada pada sidebar (Hidden)

### URL langsung ke halaman File Manager ditolak
3. Buka alamat langsung halaman File Manager
4. Verifikasi toast `You don't have permission to do this.` tampil
5. Verifikasi alamat halaman tidak dialihkan ke halaman lain
6. Verifikasi kartu `Storage Usage` tidak tampil (Hidden)

### Alamat Preview file yang sudah dihapus permanen
7. Buka alamat Preview langsung file `bukti-hapus-{runId}.pdf`
8. Verifikasi tab baru menampilkan respons tidak ditemukan untuk file `bukti-hapus-{runId}.pdf`

### Alamat Preview file milik entitas lain
9. Buka alamat Preview langsung file `dokumen-entitas-lain-{runId}.pdf`
10. Verifikasi tab baru menampilkan respons tidak ditemukan untuk file `dokumen-entitas-lain-{runId}.pdf`

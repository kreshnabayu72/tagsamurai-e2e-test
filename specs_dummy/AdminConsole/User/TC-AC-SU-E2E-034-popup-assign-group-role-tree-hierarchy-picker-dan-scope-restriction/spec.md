---
id: TC-AC-SU-E2E-034-popup-assign-group-role-tree-hierarchy-picker-dan-scope-restriction
title: "Popup Assign Group Role: Tree Picker Hirarki, Scope Restriction, dan Proteksi Duplikat"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-86
  - TC-AC-SU-87
  - TC-AC-SU-90
  - TC-AC-SU-91
  - TC-AC-SU-93
  - TC-AC-SU-256
coverage:
  web: automated
---

# Popup Assign Group Role: Tree Picker Hirarki, Scope Restriction, dan Proteksi Duplikat

## Prerequisites

- Login sebagai Total Control
- Berada di modal Assign Group Role
- Struktur grup entitas memiliki hirarki berlapis (Kantor Pusat > Divisi Regional > Cabang Area)

## Test Steps

### Navigasi Tree Picker Sekunder Select Group dan Search
1. Pada modal Assign Group Role, klik tombol `[+ Add Group]`
2. Verifikasi pop-up sekunder `Select Group` terbuka menampilkan pohon hirarki organisasi
3. Ketikkan nama grup cabang pada field input `[🔍 Search groups...]` (GAP-ACSU-E2E-001)
4. Verifikasi pohon grup menyaring secara dinamis dan hanya menampilkan cabang yang cocok dengan teks pencarian

### Invariant Exact Match dan Pembatalan
5. Centang checkbox pada node `Parent Group`
6. Verifikasi node `Children` di bawahnya TETAP UNCHECKED (Invariant exact match PRD §4.2c / §15.5: parent tidak otomatis mencentang children) (GAP-ACSU-E2E-003)
7. Klik tombol `[Cancel]` pada pop-up sekunder (GAP-ACSU-E2E-002)
8. Verifikasi pop-up tertutup dan tidak ada baris baru yang ditambahkan ke tabel modal utama

### Scope Restriction Already-Assigned dan Proteksi Duplikat
9. Buka kembali pop-up `Select Group`
10. Verifikasi grup yang sebelumnya sudah ter-assign berstatus disabled dengan tag `"Already assigned"`
11. Pilih grup yang valid dan klik `[Save]` pada pop-up sekunder
12. Verifikasi grup terpilih masuk ke daftar penugasan modal utama tanpa ada duplikasi baris

## Notes

Mengintegrasikan temuan GAP-ACSU-E2E-001, GAP-ACSU-E2E-002, dan GAP-ACSU-E2E-003.

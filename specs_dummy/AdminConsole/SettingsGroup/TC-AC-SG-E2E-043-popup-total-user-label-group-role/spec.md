---
id: TC-AC-SG-E2E-043-popup-total-user-label-group-role
title: "Hirarki prioritas label kolom Group Role pada tabel popup drill-down Total User"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-81
coverage:
  web: automated
---

# Hirarki prioritas label kolom Group Role pada tabel popup drill-down Total User

## Prerequisites

- Login sebagai Role: Total Control
- Populasi user di node mencakup: Total Control, Read Only, Group Manager di node ini, user dengan 1 role, dan user dengan 2 role

## Test Steps

### Hirarki Prioritas Label Role
1. Buka popup drill-down Total User pada node terkait
2. Amati nilai pada kolom Group Role untuk setiap baris:
   - Baris user Total Control: verifikasi tertulis teks `"Total Control"`
   - Baris user Read Only: verifikasi tertulis teks `"Read Only"`
   - Baris user Group Manager pada node ini: verifikasi tertulis teks `"Group Manager"`
   - Baris user dengan 1 penugasan Group Role biasa: verifikasi tertulis nama role-nya langsung
   - Baris user dengan 2 penugasan Group Role: verifikasi tertulis `"2 roles"`
3. Hover kursor pada teks `"2 roles"`
4. Verifikasi muncul tooltip 🔖 yang menampilkan daftar nama seluruh role yang dipegang user tersebut

## Notes

- Label Group Role memprioritaskan tingkat akses tertinggi sebelum menampilkan agregat jumlah peran.
